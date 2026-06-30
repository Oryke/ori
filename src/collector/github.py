"""
GitHub repository collector.

This module provides the first concrete implementation of the
RepositoryCollector interface for GitHub repositories.
"""

from urllib.parse import urlparse

import httpx

from .repository import RepositoryCollector
from .types import RepositoryMetadata


class GitHubCollector(RepositoryCollector):
    """Collects basic metadata from public GitHub repositories."""

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
        )

    @staticmethod
    def _parse_repository_url(repository_url: str) -> tuple[str, str]:
        """
        Extract the repository owner and name from a GitHub URL.
        """

        parsed = urlparse(repository_url)

        if parsed.netloc != "github.com":
            raise ValueError("Only GitHub repositories are currently supported.")

        parts = parsed.path.strip("/").split("/")

        if len(parts) < 2:
            raise ValueError("Invalid GitHub repository URL.")

        owner = parts[0]
        repository = parts[1]

        return owner, repository
