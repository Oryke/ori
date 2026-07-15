"""
Repository Recommendations.

Generates actionable recommendations based on repository intelligence.
"""

from collector.types import RepositoryMetadata
from intelligence.models import RepositoryDocumentation


class RecommendationEngine:
    """
    Generates repository improvement recommendations.
    """

    def recommend(
        self,
        repository: RepositoryMetadata,
        documentation: RepositoryDocumentation,
    ) -> list[str]:

        recommendations: list[str] = []

        if not documentation.has_installation:
            recommendations.append(
                "Add installation instructions to help new contributors get started."
            )

        if not documentation.has_usage_examples:
            recommendations.append(
                "Include usage examples to demonstrate how the project works."
            )

        if not repository.has_contributing_guide:
            recommendations.append(
                "Add a CONTRIBUTING.md guide for new contributors."
            )

        if not repository.has_code_of_conduct:
            recommendations.append(
                "Include a CODE_OF_CONDUCT.md to define community expectations."
            )

        if not repository.has_security_policy:
            recommendations.append(
                "Publish a SECURITY.md file explaining how vulnerabilities should be reported."
            )

        if not repository.has_issue_templates:
            recommendations.append(
                "Create issue templates to improve bug reports and feature requests."
            )

        if not repository.has_pull_request_template:
            recommendations.append(
                "Add a pull request template to standardize code reviews."
            )

        if repository.archived:
            recommendations.append(
                "This repository is archived and is not accepting new contributions."
            )

        return recommendations