"""
Repository Governance Intelligence.

Evaluates repository governance maturity using governance
signals collected by ORI.
"""

from collector.types import RepositoryMetadata
from intelligence.models import HealthDimension


# ---------------------------------------------------------------------
# Governance Scoring
# ---------------------------------------------------------------------

LICENSE_SCORE = 20
CONTRIBUTING_SCORE = 20
CODE_OF_CONDUCT_SCORE = 15
SECURITY_POLICY_SCORE = 20
ISSUE_TEMPLATE_SCORE = 10
PULL_REQUEST_TEMPLATE_SCORE = 15


class GovernanceAnalyzer:
    """
    Evaluates repository governance maturity.
    """

    def evaluate(
        self,
        repository: RepositoryMetadata,
    ) -> HealthDimension:
        """
        Evaluate repository governance maturity.
        """

        score = 0
        reasons: list[str] = []

        # -------------------------------------------------------------
        # License
        # -------------------------------------------------------------

        if repository.license:
            score += LICENSE_SCORE
            reasons.append("Open-source license detected.")
        else:
            reasons.append("No repository license detected.")

        # -------------------------------------------------------------
        # Contributing Guide
        # -------------------------------------------------------------

        if repository.has_contributing_guide:
            score += CONTRIBUTING_SCORE
            reasons.append("Contribution guide available.")
        else:
            reasons.append("No contribution guide found.")

        # -------------------------------------------------------------
        # Code of Conduct
        # -------------------------------------------------------------

        if repository.has_code_of_conduct:
            score += CODE_OF_CONDUCT_SCORE
            reasons.append("Code of Conduct detected.")
        else:
            reasons.append("Code of Conduct is missing.")

        # -------------------------------------------------------------
        # Security Policy
        # -------------------------------------------------------------

        if repository.has_security_policy:
            score += SECURITY_POLICY_SCORE
            reasons.append("Security policy detected.")
        else:
            reasons.append("No SECURITY policy found.")

        # -------------------------------------------------------------
        # Issue Templates
        # -------------------------------------------------------------

        if repository.has_issue_templates:
            score += ISSUE_TEMPLATE_SCORE
            reasons.append("Issue templates detected.")
        else:
            reasons.append("Issue templates are missing.")

        # -------------------------------------------------------------
        # Pull Request Template
        # -------------------------------------------------------------

        if repository.has_pull_request_template:
            score += PULL_REQUEST_TEMPLATE_SCORE
            reasons.append("Pull request template detected.")
        else:
            reasons.append("Pull request template is missing.")

        score = min(score, 100)

        return HealthDimension(
            score=score,
            rating=self._rating(score),
            reasons=reasons,
        )

    def _rating(
        self,
        score: int,
    ) -> str:
        """
        Convert a governance score into a human-readable rating.
        """

        if score >= 90:
            return "★★★★★ Excellent"

        if score >= 75:
            return "★★★★☆ Good"

        if score >= 50:
            return "★★★☆☆ Fair"

        if score >= 25:
            return "★★☆☆☆ Needs Improvement"

        return "★☆☆☆☆ Poor"
