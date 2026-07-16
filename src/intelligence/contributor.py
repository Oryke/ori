"""
Repository contribution advisor.

This module provides simple recommendations for developers
who want to contribute to a repository.
"""

from collector.types import RepositoryMetadata


class ContributorAdvisor:
    """Provides simple contribution advice."""

    def advise(self, repository: RepositoryMetadata) -> list[str]:
        advice = []

        if repository.language:
            advice.append(f"Recommended skill: {repository.language}")

        if repository.license:
            advice.append("This repository has an open-source license.")

        if repository.default_branch == "main":
            advice.append("Target the 'main' branch when contributing.")

        if repository.description:
            advice.append("Start by reading the README and project description.")

        return advice
