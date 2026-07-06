"""
ORI Command Line Interface.

The primary entry point into ORI.
"""

from collector.documentation import DocumentationCollector
from collector.github import GitHubCollector
from intelligence.analyzer import RepositoryAnalyzer
from intelligence.contributor import ContributorAdvisor
from intelligence.documentation import DocumentationAnalyzer
from intelligence.health import RepositoryHealthEngine
from intelligence.summarizer import RepositorySummarizer


def main() -> None:
    url = input("Repository URL: ")

    collector = GitHubCollector()
    documentation_collector = DocumentationCollector()

    repository = collector.collect(url)
    issues = collector.collect_issues(url)
    readme = documentation_collector.collect_readme(url)

    analyzer = RepositoryAnalyzer()
    insights = analyzer.analyze(repository)

    advisor = ContributorAdvisor()
    advice = advisor.advise(repository)

    health_engine = RepositoryHealthEngine()
    health = health_engine.evaluate(repository)

    documentation_analyzer = DocumentationAnalyzer()
    documentation = documentation_analyzer.analyze(readme)

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

    print("\nDocumentation")
    print("-------------")
    print(f"README: {'Yes' if documentation.has_readme else 'No'}")
    print(f"Installation Guide: {'Yes' if documentation.has_installation else 'No'}")
    print(f"Usage Examples: {'Yes' if documentation.has_usage_examples else 'No'}")
    print(f"Contributing Guide: {'Yes' if documentation.has_contributing_guide else 'No'}")
    print(f"API Documentation: {'Yes' if documentation.has_api_documentation else 'No'}")
    print(f"License Section: {'Yes' if documentation.has_license_section else 'No'}")
    print(f"Beginner Friendly: {'Yes' if documentation.beginner_friendly else 'No'}")

    print("\nSummary")
    print(f"  {documentation.summary}")

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