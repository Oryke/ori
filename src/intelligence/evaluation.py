"""
ORI Repository Evaluation Intelligence.

Combines all repository intelligence signals
into a final repository assessment.
"""

from datetime import UTC, datetime

from intelligence.models import (
    AnalysisMetadata,
    ContributorRoadmap,
    DeveloperFit,
    RepositoryDocumentation,
    RepositoryEvaluation,
    RepositoryHealth,
    RepositoryRisk,
    SkillProfile,
)


class RepositoryEvaluator:
    """
    Generates a complete repository evaluation.
    """

    def evaluate(
        self,
        health: RepositoryHealth,
        documentation: RepositoryDocumentation,
        risk: RepositoryRisk,
        skills: SkillProfile | None = None,
        developer_fit: DeveloperFit | None = None,
        roadmap: ContributorRoadmap | None = None,
    ) -> RepositoryEvaluation:
        """
        Evaluate repository quality and contributor readiness.
        """

        strengths: list[str] = []
        weaknesses: list[str] = []
        recommended_for: list[str] = []
        insights: list[str] = []

        score = 0

        # ------------------------------------------------------------
        # Health (40 points)
        # ------------------------------------------------------------

        if health:
            score += int(health.overall_score * 0.40)

            if health.overall_score >= 80:
                strengths.append("Repository demonstrates strong overall health.")
                insights.append(
                    "Repository shows strong community, maintenance, and governance signals."
                )

            else:
                weaknesses.append("Repository health signals require attention.")

        # ------------------------------------------------------------
        # Documentation (20 points)
        # ------------------------------------------------------------

        if documentation:
            documentation_score = 0

            if documentation.has_readme:
                documentation_score += 5
                strengths.append("Repository includes a README.")
            else:
                weaknesses.append("Repository is missing a README.")

            if documentation.has_installation:
                documentation_score += 5
                strengths.append("Installation instructions are available.")
            else:
                weaknesses.append("Installation instructions are missing.")

            if documentation.has_usage_examples:
                documentation_score += 5
                strengths.append("Usage examples are provided.")
            else:
                weaknesses.append("Repository lacks usage examples.")

            if documentation.has_contributing_guide:
                documentation_score += 5
                strengths.append("Contribution guidelines are available.")
            else:
                weaknesses.append("Repository has no contribution guide.")

                insights.append(
                    "Missing contributor documentation may increase onboarding difficulty."
                )
            score += documentation_score

        # ------------------------------------------------------------
        # Risk (20 points)
        # ------------------------------------------------------------

        if risk:
            score += int(risk.score * 0.20)

            if risk.score >= 80:
                strengths.append("Repository presents low adoption risk.")

            elif risk.score >= 60:
                strengths.append("Repository presents moderate adoption risk.")

            else:
                weaknesses.append("Repository has identified significant risk factors.")

        # ------------------------------------------------------------
        # Skills (10 points)
        # ------------------------------------------------------------

        if skills:
            score += 10

            strengths.append("Technical skill requirements identified.")

        # ------------------------------------------------------------
        # Developer Fit (5 points)
        # ------------------------------------------------------------

        if developer_fit:
            score += 5

            strengths.append("Contributor suitability analyzed.")

            recommended_for.append(
                f"Developers at {developer_fit.experience_level} level"
            )

        # ------------------------------------------------------------
        # Roadmap (5 points)
        # ------------------------------------------------------------

        if roadmap:
            score += 5

            strengths.append("Contribution roadmap generated.")

            recommended_for.append(roadmap.recommended_focus)

        # ------------------------------------------------------------
        # Recommendations
        # ------------------------------------------------------------

        if health and health.overall_score >= 80:
            recommended_for.extend(
                [
                    "Production use",
                    "Open-source contribution",
                ]
            )

        if documentation and documentation.has_readme:
            recommended_for.append("Learning")

        # Remove duplicates

        recommended_for = list(dict.fromkeys(recommended_for))

        score = min(score, 100)

        if score >= 90:
            rating = "★★★★★ Excellent"

        elif score >= 75:
            rating = "★★★★☆ Good"

        elif score >= 60:
            rating = "★★★☆☆ Fair"

        else:
            rating = "★★☆☆☆ Needs Improvement"

        confidence = 80

        if health:
            confidence += 5

        if documentation and documentation.has_readme:
            confidence += 5

        confidence = min(confidence, 100)

        return RepositoryEvaluation(
            overall_score=score,
            overall_rating=rating,
            metadata=AnalysisMetadata(
                generated_at=datetime.now(UTC).isoformat(),
            ),
            confidence=confidence,
            strengths=strengths,
            weaknesses=weaknesses,
            recommended_for=recommended_for,
            insights=insights,
            health=health,
            documentation=documentation,
            risk=risk,
            skills=skills,
            developer_fit=developer_fit,
            roadmap=roadmap,
        )
