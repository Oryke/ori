"""
ORI Report Generator.

Formats repository intelligence results
into human-readable reports.
"""


class RepositoryReporter:
    """
    Generates terminal reports from ORI intelligence.
    """

    def generate(
        self,
        repository,
        summary,
        health,
        documentation,
        risk,
        skills,
        developer_fit,
        roadmap,
        evaluation,
        issues,
        advice,
        insights,
    ):

        report = []

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        report.append("\nORI Analysis")
        report.append("=" * 40)

        report.append(f"\nRepository: {repository.owner}/{repository.name}")

        report.append(f"Language: {repository.language}")

        report.append(f"License: {repository.license}")

        report.append(f"Default Branch: {repository.default_branch}")

        report.append(f"URL: {repository.url}")

        # -------------------------------------------------
        # Evaluation
        # -------------------------------------------------

        report.append("\nRepository Evaluation")
        report.append("---------------------")

        report.append(f"Overall Score: {evaluation.overall_score}/100")

        report.append(f"Overall Rating: {evaluation.overall_rating}")

        report.append("\nConfidence")
        report.append("-----------------")
        report.append(f"Confidence: {evaluation.confidence}%")

        # -------------------------------------------------
        # Strengths
        # -------------------------------------------------

        report.append("\nStrengths")
        report.append("---------")

        for item in evaluation.strengths:
            report.append(f"✓ {item}")

        # -------------------------------------------------
        # Weaknesses
        # -------------------------------------------------

        report.append("\nWeaknesses")
        report.append("----------")

        for item in evaluation.weaknesses:
            report.append(f"• {item}")

        # -------------------------------------------------
        # Insights
        # -------------------------------------------------

        if evaluation.insights:
            report.append("\nEvaluation Insights")
            report.append("-------------------")

            for insight in evaluation.insights:
                report.append(f"• {insight}")

        # -------------------------------------------------
        # Advice
        # -------------------------------------------------

        report.append("\nAdvice")
        report.append("------")

        for item in advice:
            report.append(f"- {item}")

        # -------------------------------------------------
        # Issues
        # -------------------------------------------------

        report.append("\nOpen Issues")
        report.append("-----------")

        for issue in issues[:5]:
            report.append(f"#{issue.number} - {issue.title}")

        return "\n".join(report)
