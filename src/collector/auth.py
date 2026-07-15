"""
GitHub authentication utilities.

Provides authenticated request headers for GitHub API requests.
"""

from __future__ import annotations

import os


class GitHubAuth:
    """
    Provides request headers for the GitHub API.
    """

    USER_AGENT = "ORI"

    @classmethod
    def headers(cls) -> dict[str, str]:
        """
        Return headers for GitHub API requests.

        If a GitHub Personal Access Token is available through the
        GITHUB_TOKEN environment variable, authenticated requests
        are used automatically.
        """

        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": cls.USER_AGENT,
        }

        token = os.getenv("GITHUB_TOKEN")

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return headers