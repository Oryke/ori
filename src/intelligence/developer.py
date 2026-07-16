"""
Developer Fit Intelligence.

Evaluates how suitable a repository is for
prospective contributors.
"""

from collector.types import RepositoryMetadata
from intelligence.models import (
    DeveloperFit,
    RepositoryDocumentation,
)


class DeveloperFitAnalyzer:
    """
    Evaluates developer fit.
    """

    def evaluate(
        self,
        repository: RepositoryMetadata,
        documentation: RepositoryDocumentation,
    ) -> DeveloperFit:
        """
        Evaluate repository suitability.
        """

        return DeveloperFit(
            experience_level="Intermediate",
            estimated_onboarding="2-3 days",
            confidence=90,
            recommended_skills=[],
            recommended_contributions=[],
            reasons=[],
        )
