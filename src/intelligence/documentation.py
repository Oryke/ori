"""
Repository Documentation Analyzer.

Analyzes repository documentation collected by ORI.
"""

from intelligence.constants import (
    INSTALLATION_KEYWORDS,
    USAGE_KEYWORDS,
)
from intelligence.models import RepositoryDocumentation


class DocumentationAnalyzer:
    """
    Analyzes repository documentation.
    """

    def analyze(self, readme: str) -> RepositoryDocumentation:
        """
        Analyze a repository README.
        """

        normalized = readme.lower()

        has_readme = bool(readme.strip())

        return RepositoryDocumentation(
            has_readme=has_readme,
            has_installation=self._has_installation(normalized),
            has_usage_examples=self._has_usage_examples(normalized),
            has_contributing_guide=False,
            has_api_documentation=False,
            has_license_section=False,
            beginner_friendly=False,
            summary=(
                "Repository documentation analyzed. "
                "Additional documentation intelligence "
                "will be introduced in future releases."
            ),
        )

    def _has_installation(self, normalized: str) -> bool:
        """
        Determine whether the repository provides
        installation instructions.
        """

        return any(
            keyword in normalized
            for keyword in INSTALLATION_KEYWORDS
        )

    def _has_usage_examples(self, normalized: str) -> bool:
        """
        Determine whether the repository provides
        usage examples.
        """

        return any(
            keyword in normalized
            for keyword in USAGE_KEYWORDS
        )