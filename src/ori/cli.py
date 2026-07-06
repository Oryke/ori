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

    health = RepositoryHealthEngine()
    assessment = health.assess(repository)

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

    for key, value in assessment.items():
        print(f"- {key}: {value}")

    print("\nInsights")
    print("----------")

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