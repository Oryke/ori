"""
Developer Fit Intelligence.

Evaluates how suitable a repository is for a potential contributor
based on repository complexity, documentation, skills, and maturity.
"""

from collector.types import RepositoryMetadata
from intelligence.models import (
    DeveloperFit,
    RepositoryDocumentation,
    SkillProfile,
)


class DeveloperFitAnalyzer:
    """
    Evaluates contributor suitability for a repository.
    """

    def evaluate(
        self,
        repository: RepositoryMetadata,
        documentation: RepositoryDocumentation,
        skills: SkillProfile,
    ) -> DeveloperFit:
        """
        Produce a developer fit assessment.
        """

        reasons: list[str] = []
        recommended_contributions: list[str] = []

        # ---------------------------------------------------------
        # Determine experience level
        # ---------------------------------------------------------

        if repository.stars >= 10000:
            experience_level = "Intermediate to Advanced"

            reasons.append(
                "Large community adoption indicates a mature project."
            )

        elif repository.stars >= 1000:
            experience_level = "Intermediate"

            reasons.append(
                "Repository has enough adoption to require contributor familiarity."
            )

        else:
            experience_level = "Beginner Friendly"

            reasons.append(
                "Repository size suggests easier entry for new contributors."
            )

        # ---------------------------------------------------------
        # Documentation impact
        # ---------------------------------------------------------

        if documentation.has_contributing_guide:
            reasons.append(
                "Contribution guidelines improve contributor onboarding."
            )
        else:
            reasons.append(
                "Missing contribution documentation may increase onboarding difficulty."
            )

        # ---------------------------------------------------------
        # Estimate onboarding time
        # ---------------------------------------------------------

        if skills.difficulty == "Advanced":
            onboarding = "2-4 weeks"

        elif skills.difficulty == "Intermediate":
            onboarding = "1-2 weeks"

        else:
            onboarding = "A few days"

        # ---------------------------------------------------------
        # Suggested contribution areas
        # ---------------------------------------------------------

        recommended_contributions.extend(
            [
                "Documentation improvements",
                "Bug fixes",
                "Issue discussions",
            ]
        )

        if repository.open_issues > 0:
            recommended_contributions.append(
                "Review and resolve open issues"
            )

        return DeveloperFit(
            experience_level=experience_level,
            estimated_onboarding=onboarding,
            confidence=self._confidence(
                repository,
                documentation,
            ),
            recommended_skills=skills.required_skills,
            recommended_contributions=recommended_contributions,
            reasons=reasons,
        )

    def _confidence(
        self,
        repository: RepositoryMetadata,
        documentation: RepositoryDocumentation,
    ) -> int:
        """
        Calculate confidence level for the assessment.
        """

        score = 50

        if repository.language:
            score += 15

        if documentation.has_readme:
            score += 15

        if documentation.has_contributing_guide:
            score += 20

        return min(score, 100)