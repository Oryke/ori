"""
GitHub repository collector.

This module provides the first concrete implementation of the
RepositoryCollector interface for GitHub repositories.
"""

import base64
from urllib.parse import urlparse

import httpx

from .repository import RepositoryCollector
from .types import IssueMetadata, RepositoryMetadata


class GitHubCollector(RepositoryCollector):
    """Collects information from public GitHub repositories."""

    GITHUB_API = "https://api.github.com/repos"

    def collect(self, repository_url: str) -> RepositoryMetadata:
        """
        Collect basic metadata for a public GitHub repository.
        """

        owner, repository = self._parse_repository_url(repository_url)

        response = httpx.get(
            f"{self.GITHUB_API}/{owner}/{repository}",
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "ORI",
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        license_info = data.get("license")

        return RepositoryMetadata(
            name=data["name"],
            owner=data["owner"]["login"],
            url=data["html_url"],
            description=data.get("description"),
            default_branch=data.get("default_branch"),
            license=license_info["spdx_id"] if license_info else None,
            language=data.get("language"),
            stars=data.get("stargazers_count", 0),
            forks=data.get("forks_count", 0),
            watchers=data.get("subscribers_count", 0),
            open_issues=data.get("open_issues_count", 0),
        )

    def collect_issues(self, repository_url: str) -> list[IssueMetadata]:
        """
        Collect open issues for a public GitHub repository.
        """

        owner, repository = self._parse_repository_url(repository_url)

        response = httpx.get(
            f"{self.GITHUB_API}/{owner}/{repository}/issues",
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "ORI",
            },
            timeout=30,
        )

        response.raise_for_status()

        issues = []

        for item in response.json():

            # Skip pull requests.
            if "pull_request" in item:
                continue

            issues.append(
                IssueMetadata(
                    number=item["number"],
                    title=item["title"],
                    url=item["html_url"],
                    labels=[label["name"] for label in item["labels"]],
                    state=item["state"],
                )
            )

        return issues

    def collect_readme(self, repository_url: str) -> str:
        """
        Collect the repository README as plain text.
        """

        owner, repository = self._parse_repository_url(repository_url)

        response = httpx.get(
            f"{self.GITHUB_API}/{owner}/{repository}/readme",
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "ORI",
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        content = data.get("content", "")

        if not content:
            return ""

        return base64.b64decode(content).decode("utf-8")

    @staticmethod
    def _parse_repository_url(repository_url: str) -> tuple[str, str]:
        """
        Extract the repository owner and name from a GitHub URL.
        """

        parsed = urlparse(repository_url)

        if parsed.netloc != "github.com":
            raise ValueError(
                "Only GitHub repositories are currently supported."
            )

        parts = parsed.path.strip("/").split("/")

        if len(parts) != 2:
            raise ValueError(
                "Expected a GitHub repository URL in the form "
                "'https://github.com/<owner>/<repository>'."
            )

        owner = parts[0]
        repository = parts[1]

        return owner, repository