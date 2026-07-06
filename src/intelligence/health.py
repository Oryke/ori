"""
Repository Health Engine.

Evaluates the overall health of a repository using
repository intelligence signals.
"""

from collector.types import RepositoryMetadata
from intelligence.models import HealthDimension, RepositoryHealth

# ---------------------------------------------------------------------
# Community Scoring Configuration
# ---------------------------------------------------------------------

STAR_THRESHOLDS: list[tuple[int, int]] = [
    (500, 40),
    (100, 30),
    (50, 20),
    (10, 10),
]

FORK_THRESHOLDS: list[tuple[int, int]] = [
    (100, 35),
    (50, 30),
    (20, 20),
    (5, 10),
]

WATCHER_THRESHOLDS: list[tuple[int, int]] = [
    (100, 25),
    (50, 20),
    (20, 10),
    (5, 5),
]


class RepositoryHealthEngine:
    """Evaluates the health of a repository."""

    def evaluate(self, repository: RepositoryMetadata) -> RepositoryHealth:
        """Return ORI's overall health evaluation."""

        community = self._evaluate_community(repository)
        maintenance = self._evaluate_maintenance(repository)
        governance = self._evaluate_governance(repository)

        overall_score = (
            community.score
            + maintenance.score
            + governance.score
        ) // 3

        return RepositoryHealth(
            overall_score=overall_score,
            overall_rating=self._rating_for_score(overall_score),
            overall_reasons=[
                "Overall health is derived from community, maintenance, and governance signals.",
            ],
            community=community,
            maintenance=maintenance,
            governance=governance,
        )

    def _normalize(
        self,
        value: int,
        thresholds: list[tuple[int, int]],
    ) -> int:
        """
        Convert a repository metric into a normalized score.

        Thresholds should be ordered from highest to lowest.
        """

        for minimum, points in thresholds:
            if value >= minimum:
                return points

        return 0

    def _evaluate_community(
        self,
        repository: RepositoryMetadata,
    ) -> HealthDimension:
        """Evaluate repository community health."""

        star_score = self._normalize(
            repository.stars,
            STAR_THRESHOLDS,
        )

        fork_score = self._normalize(
            repository.forks,
            FORK_THRESHOLDS,
        )

        watcher_score = self._normalize(
            repository.watchers,
            WATCHER_THRESHOLDS,
        )

        community_score = (
            star_score
            + fork_score
            + watcher_score
        )

        reasons: list[str] = []

        if repository.stars >= 500:
            reasons.append(
                "Strong community adoption."
            )
        elif repository.stars >= 100:
            reasons.append(
                "Growing community adoption."
            )
        else:
            reasons.append(
                "Community adoption is still developing."
            )

        if repository.forks >= 100:
            reasons.append(
                "High contributor interest."
            )
        elif repository.forks >= 20:
            reasons.append(
                "Contributors are actively engaging with the project."
            )

        if repository.watchers >= 100:
            reasons.append(
                "Strong ongoing community engagement."
            )
        elif repository.watchers >= 20:
            reasons.append(
                "Community members are following project updates."
            )

        return HealthDimension(
            score=community_score,
            rating=self._rating_for_score(community_score),
            reasons=reasons,
        )

    def _evaluate_maintenance(
        self,
        repository: RepositoryMetadata,
    ) -> HealthDimension:
        """Evaluate repository maintenance health."""

        return HealthDimension(
            score=100,
            rating="★★★★★ Excellent",
            reasons=[
                "Maintenance evaluation has not been implemented yet.",
            ],
        )

    def _evaluate_governance(
        self,
        repository: RepositoryMetadata,
    ) -> HealthDimension:
        """Evaluate repository governance health."""

        return HealthDimension(
            score=100,
            rating="★★★★★ Excellent",
            reasons=[
                "Governance evaluation has not been implemented yet.",
            ],
        )

    def _rating_for_score(self, score: int) -> str:
        """Return a rating for a health score."""

        if score >= 80:
            return "★★★★★ Excellent"

        if score >= 60:
            return "★★★★☆ Good"

        if score >= 40:
            return "★★★☆☆ Fair"

        return "★★☆☆☆ Needs Attention"