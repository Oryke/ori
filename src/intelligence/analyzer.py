"""
Repository analysis engine.

This module transforms raw repository metadata into simple repository insights.
"""

from collector.types import RepositoryMetadata


class RepositoryAnalyzer:
    """Analyze repository metadata to produce simple insights."""

    def analyze(self, repository: RepositoryMetadata) -> dict[str, str]:
        """
        Analyze a repository and return simple insights.
        """

        return {
            "Primary Language": repository.language or "Unknown",
            "Project Type": self._detect_project_type(repository),
        }

    def _detect_project_type(
        self,
        repository: RepositoryMetadata,
    ) -> str:
        """
        Infer a project type from the available metadata.
        """

        if repository.language == "Python":
            return "Python Project"

        if repository.language == "JavaScript":
            return "JavaScript Project"

        if repository.language == "TypeScript":
            return "TypeScript Project"

        return "Unknown Project"