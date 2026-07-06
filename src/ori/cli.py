"""
ORI Command Line Interface.

The primary entry point into ORI.
"""

from collector.github import GitHubCollector
from intelligence.analyzer import RepositoryAnalyzer
from intelligence.contributor import ContributorAdvisor
from intelligence.health import RepositoryHealthEngine
from intelligence.summarizer import RepositorySummarizer


def main() -> None:
    url = input("Repository URL: ")

    collector = GitHubCollector()

    repository = collector.collect(url)
    issues = collector.collect_issues(url)

    analyzer = RepositoryAnalyzer()
    insights = analyzer.analyze(repository)

    advisor = ContributorAdvisor()
    advice = advisor.advise(repository)

    health_engine = RepositoryHealthEngine()
    health = health_engine.evaluate(repository)

    summarizer = RepositorySummarizer()
    summary = summarizer.summarize(repository)

    print("\nORI Analysis")
    print("=" * 40)

    print(f"\nRepository: {repository.owner}/{repository.name}")
    print(f"Language: {repository.language}")
    print(f"License: {repository.license}")
    print(f"Default Branch: {repository.default_branch}")
    print(f"URL: {repository.url}")

    print("\nRepository Statistics")
    print("---------------------")
    print(f"Stars: {repository.stars}")
    print(f"Forks: {repository.forks}")
    print(f"Watchers: {repository.watchers}")
    print(f"Open Issues: {repository.open_issues}")

    print("\nSummary")
    print("-------")
    print(summary)

    print("\nRepository Health")
    print("-----------------")

    print("\nOverall")
    print(f"  Score : {health.overall_score}/100")
    print(f"  Rating: {health.overall_rating}")

    if health.overall_reasons:
        print("  Reasons:")
        for reason in health.overall_reasons:
            print(f"    • {reason}")

    print("\nCommunity")
    print(f"  Score : {health.community.score}/100")
    print(f"  Rating: {health.community.rating}")

    if health.community.reasons:
        print("  Reasons:")
        for reason in health.community.reasons:
            print(f"    • {reason}")

    print("\nMaintenance")
    print(f"  Score : {health.maintenance.score}/100")
    print(f"  Rating: {health.maintenance.rating}")

    if health.maintenance.reasons:
        print("  Reasons:")
        for reason in health.maintenance.reasons:
            print(f"    • {reason}")

    print("\nGovernance")
    print(f"  Score : {health.governance.score}/100")
    print(f"  Rating: {health.governance.rating}")

    if health.governance.reasons:
        print("  Reasons:")
        for reason in health.governance.reasons:
            print(f"    • {reason}")

    print("\nInsights")
    print("--------")

    for key, value in insights.items():
        print(f"- {key}: {value}")

    print("\nAdvice")
    print("------")

    for item in advice:
        print(f"- {item}")

    print("\nOpen Issues")
    print("-----------")

    for issue in issues[:5]:
        print(f"#{issue.number} - {issue.title}")


if __name__ == "__main__":
    main()