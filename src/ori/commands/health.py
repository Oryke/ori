"""
ORI Health Command.

Displays repository health intelligence.
"""

from collector.github import GitHubCollector
from intelligence.health import RepositoryHealthEngine


def run(repository_url: str) -> None:
    """
    Analyze and display repository health.
    """

    collector = GitHubCollector()

    repository = collector.collect(repository_url)

    health_engine = RepositoryHealthEngine()

    health = health_engine.evaluate(repository)

    print()
    print("ORI Repository Health")
    print("=" * 40)

    print(f"Score: {health.overall_score}/100")
    print(f"Rating: {health.overall_rating}")

    print()
    print("Health Analysis")
    print("-" * 40)

    for reason in health.overall_reasons:
        print(f"✓ {reason}")

    print()

    if health.community:
        print("Community")
        print("-" * 40)

        print(f"Score: {health.community.score}")
        print(f"Rating: {health.community.rating}")

        for reason in health.community.reasons:
            print(f"✓ {reason}")

        print()

    if health.maintenance:
        print("Maintenance")
        print("-" * 40)

        print(f"Score: {health.maintenance.score}")
        print(f"Rating: {health.maintenance.rating}")

        for reason in health.maintenance.reasons:
            print(f"✓ {reason}")

        print()

    if health.governance:
        print("Governance")
        print("-" * 40)

        print(f"Score: {health.governance.score}")
        print(f"Rating: {health.governance.rating}")

        for reason in health.governance.reasons:
            print(f"✓ {reason}")