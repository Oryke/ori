"""
Repository Health Engine.

Evaluates the overall health of a repository using
basic repository signals.
"""

from collector.types import RepositoryMetadata


class RepositoryHealthEngine:
    """Computes a simple repository health assessment."""

    def assess(self, repository: RepositoryMetadata) -> dict[str, str]:
        score = 0

        if repository.license:
            score += 20

        if repository.description:
            score += 20

        if repository.default_branch:
            score += 20

        if repository.language:
            score += 20

        score += 20

        if score >= 80:
            rating = "★★★★★ Excellent"

        elif score >= 60:
            rating = "★★★★☆ Good"

        elif score >= 40:
            rating = "★★★☆☆ Fair"

        else:
            rating = "★★☆☆☆ Needs Attention"

        return {
            "Score": f"{score}/100",
            "Rating": rating,
        }