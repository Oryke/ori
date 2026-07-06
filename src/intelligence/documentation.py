"""
Repository Documentation Analyzer.

Analyzes repository documentation collected by ORI.
"""

from intelligence.models import RepositoryDocumentation

# ---------------------------------------------------------------------
# Documentation Detection Keywords
# ---------------------------------------------------------------------

INSTALLATION_KEYWORDS = (
    "installation",
    "install",
    "pip install",
    "poetry install",
    "conda install",
    "npm install",
    "cargo install",
)


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

        has_installation = any(
            keyword in normalized
            for keyword in INSTALLATION_KEYWORDS
        )

        return RepositoryDocumentation(
            has_readme=has_readme,
            has_installation=has_installation,
            has_usage_examples=False,
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