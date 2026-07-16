"""
Tests for the Repository Health Engine.
"""

from datetime import UTC, datetime, timedelta

from collector.types import RepositoryMetadata
from intelligence.health import RepositoryHealthEngine


def make_repository(
    *,
    stars: int = 0,
    forks: int = 0,
    watchers: int = 0,
    archived: bool = False,
    last_push: str | None = None,
) -> RepositoryMetadata:
    """Create a repository with sensible defaults for testing."""

    return RepositoryMetadata(
        owner="psf",
        name="requests",
        description="A test repository",
        language="Python",
        license="MIT",
        default_branch="main",
        url="https://github.com/psf/requests",
        stars=stars,
        forks=forks,
        watchers=watchers,
        open_issues=0,
        archived=archived,
        last_push=last_push,
    )


def test_popular_repository_has_excellent_community_score():
    engine = RepositoryHealthEngine()

    repository = make_repository(
        stars=500,
        forks=100,
        watchers=100,
    )

    health = engine.evaluate(repository)

    assert health.community is not None
    assert health.community.score == 100
    assert health.community.rating == "★★★★★ Excellent"


def test_small_repository_has_lower_community_score():
    engine = RepositoryHealthEngine()

    repository = make_repository(
        stars=5,
        forks=2,
        watchers=1,
    )

    health = engine.evaluate(repository)

    assert health.community is not None
    assert health.community.score == 0
    assert health.community.rating == "★★☆☆☆ Needs Attention"


def test_recently_updated_repository_scores_high_for_maintenance():
    engine = RepositoryHealthEngine()

    recent_push = (
        datetime.now(UTC) - timedelta(days=5)
    ).isoformat()

    repository = make_repository(
        last_push=recent_push,
    )

    health = engine.evaluate(repository)

    assert health.maintenance is not None
    assert health.maintenance.score == 100
    assert health.maintenance.rating == "★★★★★ Excellent"


def test_archived_repository_has_zero_maintenance_score():
    engine = RepositoryHealthEngine()

    repository = make_repository(
        archived=True,
    )

    health = engine.evaluate(repository)

    assert health.maintenance is not None
    assert health.maintenance.score == 0
    assert health.maintenance.rating == "★★☆☆☆ Needs Attention"


def test_overall_health_contains_all_dimensions():
    engine = RepositoryHealthEngine()

    recent_push = (
        datetime.now(UTC) - timedelta(days=10)
    ).isoformat()

    repository = make_repository(
        stars=600,
        forks=120,
        watchers=150,
        last_push=recent_push,
    )

    health = engine.evaluate(repository)

    assert health.community is not None
    assert health.maintenance is not None
    assert health.governance is not None
    assert health.overall_score >= 0
    assert health.overall_rating != ""