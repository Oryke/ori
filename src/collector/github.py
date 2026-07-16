"""
GitHub repository collector.

Provides ORI's GitHub implementation for collecting repository
metadata, issues, documentation, and governance signals.
"""

import base64
import time
from urllib.parse import urlparse

import httpx

from .auth import GitHubAuth
from .repository import RepositoryCollector
from .types import IssueMetadata, RepositoryMetadata


class GitHubCollector(RepositoryCollector):
    """
    Collects intelligence from public GitHub repositories.
    """

    GITHUB_API = "https://api.github.com/repos"

    def __init__(self) -> None:
        """
        Initialize the collector.
        """

        self._contents_cache: dict[
            tuple[str, str],
            set[str],
        ] = {}

    # ------------------------------------------------------------------
    # HTTP Request Helper
    # ------------------------------------------------------------------

    def _request(
        self,
        url: str,
    ) -> httpx.Response:
        """
        Perform a resilient GitHub API request.
        """

        attempts = 3

        for attempt in range(attempts):
            try:
                response = httpx.get(
                    url,
                    headers=GitHubAuth.headers(),
                    timeout=30,
                )

                response.raise_for_status()

                return response

            except httpx.ConnectError:
                if attempt == attempts - 1:
                    raise

                time.sleep(2)

        raise RuntimeError("Unable to connect to GitHub API.")

    # ------------------------------------------------------------------
    # Repository
    # ------------------------------------------------------------------

    def collect(
        self,
        repository_url: str,
    ) -> RepositoryMetadata:
        """
        Collect repository metadata from GitHub.
        """

        owner, repository = self._parse_repository_url(repository_url)

        response = self._request(f"{self.GITHUB_API}/{owner}/{repository}")

        data = response.json()

        license_info = data.get("license")

        default_branch = data.get("default_branch")

        return RepositoryMetadata(
            name=data["name"],
            owner=data["owner"]["login"],
            url=data["html_url"],
            description=data.get("description"),
            default_branch=default_branch,
            license=(license_info["spdx_id"] if license_info else None),
            language=data.get("language"),
            stars=data.get(
                "stargazers_count",
                0,
            ),
            forks=data.get(
                "forks_count",
                0,
            ),
            watchers=data.get(
                "subscribers_count",
                0,
            ),
            open_issues=data.get(
                "open_issues_count",
                0,
            ),
            archived=data.get(
                "archived",
                False,
            ),
            last_push=data.get("pushed_at"),
            last_update=data.get("updated_at"),
            default_branch_protected=self._branch_protected(
                owner,
                repository,
                default_branch,
            ),
            has_contributing_guide=self._find_file(
                owner,
                repository,
                "CONTRIBUTING.md",
                "CONTRIBUTING",
                "docs/CONTRIBUTING.md",
            ),
            has_code_of_conduct=self._find_file(
                owner,
                repository,
                "CODE_OF_CONDUCT.md",
                "CODE_OF_CONDUCT",
                ".github/CODE_OF_CONDUCT.md",
            ),
            has_security_policy=self._find_file(
                owner,
                repository,
                "SECURITY.md",
                "SECURITY",
                ".github/SECURITY.md",
            ),
            has_issue_templates=self._directory_exists(
                owner,
                repository,
                ".github/ISSUE_TEMPLATE",
            ),
            has_pull_request_template=self._find_file(
                owner,
                repository,
                ".github/PULL_REQUEST_TEMPLATE.md",
                "PULL_REQUEST_TEMPLATE.md",
                "docs/PULL_REQUEST_TEMPLATE.md",
            ),
        )

        # ------------------------------------------------------------------

    # Issues
    # ------------------------------------------------------------------

    def collect_issues(
        self,
        repository_url: str,
    ) -> list[IssueMetadata]:
        """
        Collect open GitHub issues.
        """

        owner, repository = self._parse_repository_url(repository_url)

        response = self._request(f"{self.GITHUB_API}/{owner}/{repository}/issues")

        issues: list[IssueMetadata] = []

        for item in response.json():
            # Ignore pull requests

            if "pull_request" in item:
                continue

            issues.append(
                IssueMetadata(
                    number=item["number"],
                    title=item["title"],
                    url=item["html_url"],
                    labels=[label["name"] for label in item.get("labels", [])],
                    state=item["state"],
                )
            )

        return issues

    # ------------------------------------------------------------------
    # README
    # ------------------------------------------------------------------

    def collect_readme(
        self,
        repository_url: str,
    ) -> str:
        """
        Collect the repository README.
        """

        owner, repository = self._parse_repository_url(repository_url)

        response = self._request(f"{self.GITHUB_API}/{owner}/{repository}/readme")

        encoded = response.json().get("content")

        if not encoded:
            return ""

        return base64.b64decode(encoded).decode(
            "utf-8",
            errors="ignore",
        )

    # ------------------------------------------------------------------
    # Governance Helpers
    # ------------------------------------------------------------------

    def _find_file(
        self,
        owner: str,
        repository: str,
        *paths: str,
    ) -> bool:
        """
        Determine whether any candidate file exists.
        """

        return any(
            self._request_contents(
                owner,
                repository,
                path,
            )
            for path in paths
        )

    def _directory_exists(
        self,
        owner: str,
        repository: str,
        path: str,
    ) -> bool:
        """
        Determine whether a directory exists.
        """

        return self._request_contents(
            owner,
            repository,
            path,
        )

    def _request_contents(
        self,
        owner: str,
        repository: str,
        path: str,
    ) -> bool:
        """
        Check repository contents using a small cache.
        """

        cache_key = (
            owner,
            repository,
        )

        if cache_key not in self._contents_cache:
            self._contents_cache[cache_key] = set()

        if path in self._contents_cache[cache_key]:
            return True

        try:
            self._request(f"{self.GITHUB_API}/{owner}/{repository}/contents/{path}")

            self._contents_cache[cache_key].add(path)

            return True

        except httpx.HTTPStatusError:
            return False

    def _branch_protected(
        self,
        owner: str,
        repository: str,
        branch: str | None,
    ) -> bool:
        """
        Determine whether the default branch is protected.
        """

        if not branch:
            return False

        try:
            response = self._request(
                f"{self.GITHUB_API}/{owner}/{repository}/branches/{branch}"
            )

            return response.json().get(
                "protected",
                False,
            )

        except httpx.HTTPStatusError:
            return False

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_repository_url(
        repository_url: str,
    ) -> tuple[str, str]:
        """
        Extract the repository owner and name from a GitHub URL.
        """

        parsed = urlparse(repository_url.strip())

        if parsed.netloc not in (
            "github.com",
            "www.github.com",
        ):
            raise ValueError("Only GitHub repositories are currently supported.")

        parts = parsed.path.strip("/").split("/")

        if len(parts) < 2:
            raise ValueError(
                "Expected URL format: 'https://github.com/<owner>/<repository>'."
            )

        owner = parts[0]
        repository = parts[1].removesuffix(".git")

        return owner, repository
