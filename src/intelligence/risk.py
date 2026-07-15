"""
Repository Risk Analyzer.

Evaluates repository adoption risk using repository metadata,
documentation quality, governance practices, and maintenance
signals.
"""

from datetime import datetime, timezone

from collector.types import RepositoryMetadata
from intelligence.models import (
    RepositoryDocumentation,
    RepositoryRisk,
)

ACTIVE_DAYS = 365
HIGH_ISSUE_THRESHOLD = 500


class RepositoryRiskAnalyzer:
    """
    Evaluates repository adoption risk.
    """

    def evaluate(
        self,
        repository: RepositoryMetadata,
        documentation: RepositoryDocumentation,
    ) -> RepositoryRisk:

        score = 100

        reasons: list[str] = []
        warnings: list[str] = []

        # ---------------------------------------------------------
        # Repository Status
        # ---------------------------------------------------------

        if repository.archived:
            score -= 35
            warnings.append(
                "Repository has been archived."
            )
        else:
            reasons.append(
                "Repository is actively maintained."
            )

        # ---------------------------------------------------------
        # Recent Development Activity
        # ---------------------------------------------------------

        if repository.last_push:

            pushed = datetime.fromisoformat(
                repository.last_push.replace(
                    "Z",
                    "+00:00",
                )
            )

            age = (
                datetime.now(timezone.utc)
                - pushed
            ).days

            if age <= 90:
                reasons.append(
                    "Recent development activity detected."
                )

            elif age <= ACTIVE_DAYS:
                score -= 10
                warnings.append(
                    f"Last code update was {age} days ago."
                )

            else:
                score -= 25
                warnings.append(
                    f"Repository appears inactive ({age} days)."
                )

        # ---------------------------------------------------------
        # License
        # ---------------------------------------------------------

        if repository.license:
            reasons.append(
                "Open-source license detected."
            )
        else:
            score -= 20
            warnings.append(
                "Repository does not define a license."
            )

        # ---------------------------------------------------------
        # Governance
        # ---------------------------------------------------------

        if repository.has_security_policy:
            reasons.append(
                "Security policy available."
            )
        else:
            score -= 10
            warnings.append(
                "Missing SECURITY.md."
            )

        if repository.has_code_of_conduct:
            reasons.append(
                "Code of Conduct available."
            )
        else:
            score -= 5
            warnings.append(
                "No Code of Conduct found."
            )

        if repository.has_contributing_guide:
            reasons.append(
                "Contribution guidelines available."
            )
        else:
            score -= 5
            warnings.append(
                "Missing CONTRIBUTING.md."
            )

        if repository.has_issue_templates:
            reasons.append(
                "Issue templates available."
            )

        if repository.has_pull_request_template:
            reasons.append(
                "Pull request template available."
            )

        # ---------------------------------------------------------
        # Documentation
        # ---------------------------------------------------------

        if documentation.has_installation:
            reasons.append(
                "Installation instructions available."
            )
        else:
            score -= 5
            warnings.append(
                "Installation instructions missing."
            )

        if documentation.has_usage_examples:
            reasons.append(
                "Usage examples available."
            )
        else:
            score -= 5
            warnings.append(
                "Usage examples missing."
            )

        if documentation.beginner_friendly:
            reasons.append(
                "Beginner-friendly documentation."
            )

        # ---------------------------------------------------------
        # Community
        # ---------------------------------------------------------

        if repository.stars >= 100:
            reasons.append(
                "Repository has strong community adoption."
            )

        if repository.open_issues >= HIGH_ISSUE_THRESHOLD:
            score -= 5
            warnings.append(
                "Large number of open issues."
            )

        score = max(min(score, 100), 0)

        return RepositoryRisk(
            score=score,
            level=self._level(score),
            reasons=reasons,
            warnings=warnings,
            recommendation=self._recommendation(score),
        )

    def _level(
        self,
        score: int,
    ) -> str:

        if score >= 90:
            return "VERY LOW"

        if score >= 80:
            return "LOW"

        if score >= 65:
            return "MODERATE"

        if score >= 45:
            return "HIGH"

        return "VERY HIGH"

    def _recommendation(
        self,
        score: int,
    ) -> str:

        if score >= 90:
            return (
                "Excellent candidate for production adoption."
            )

        if score >= 80:
            return (
                "Suitable for production use."
            )

        if score >= 65:
            return (
                "Suitable after normal technical review."
            )

        if score >= 45:
            return (
                "Adopt with caution and perform a detailed review."
            )

        return (
            "High adoption risk. Resolve identified issues before use."
        )