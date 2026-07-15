"""
Repository Documentation Analyzer.

Analyzes repository documentation collected by ORI.
"""

from intelligence.constants import (
    INSTALLATION_KEYWORDS,
    USAGE_KEYWORDS,
)
from intelligence.models import RepositoryDocumentation


CONTRIBUTING_KEYWORDS = (
    "contributing",
    "how to contribute",
    "contribution guide",
)

API_KEYWORDS = (
    "api",
    "reference",
    "api reference",
    "rest api",
    "graphql",
)

LICENSE_KEYWORDS = (
    "license",
    "licensed under",
    "copyright",
)

BEGINNER_KEYWORDS = (
    "good first issue",
    "beginner",
    "first contribution",
    "first issue",
    "help wanted",
    "easy",
)


class DocumentationAnalyzer:
    """
    Analyzes repository documentation.
    """

    def analyze(
        self,
        readme: str,
    ) -> RepositoryDocumentation:
        """
        Analyze a repository README.
        """

        normalized = readme.lower()

        has_readme = bool(readme.strip())

        has_installation = self._contains_any(
            normalized,
            INSTALLATION_KEYWORDS,
        )

        has_usage_examples = self._contains_any(
            normalized,
            USAGE_KEYWORDS,
        )

        has_contributing_guide = self._contains_any(
            normalized,
            CONTRIBUTING_KEYWORDS,
        )

        has_api_documentation = self._contains_any(
            normalized,
            API_KEYWORDS,
        )

        has_license_section = self._contains_any(
            normalized,
            LICENSE_KEYWORDS,
        )

        beginner_friendly = self._contains_any(
            normalized,
            BEGINNER_KEYWORDS,
        )

        score = sum(
            [
                has_readme,
                has_installation,
                has_usage_examples,
                has_contributing_guide,
                has_api_documentation,
                has_license_section,
                beginner_friendly,
            ]
        )

        if score >= 6:
            summary = (
                "Excellent documentation with comprehensive "
                "onboarding information."
            )
        elif score >= 4:
            summary = (
                "Good documentation covering most contributor needs."
            )
        elif score >= 2:
            summary = (
                "Basic documentation is available but could be improved."
            )
        else:
            summary = (
                "Documentation is minimal and may make onboarding difficult."
            )

        return RepositoryDocumentation(
            has_readme=has_readme,
            has_installation=has_installation,
            has_usage_examples=has_usage_examples,
            has_contributing_guide=has_contributing_guide,
            has_api_documentation=has_api_documentation,
            has_license_section=has_license_section,
            beginner_friendly=beginner_friendly,
            summary=summary,
        )

    def _contains_any(
        self,
        text: str,
        keywords: tuple[str, ...] | list[str],
    ) -> bool:
        """
        Determine whether any keyword exists in the text.
        """

        return any(
            keyword in text
            for keyword in keywords
        )