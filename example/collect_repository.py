"""
Example demonstrating ORI's first repository collection.

Run with:

    python -m example.collect_repository
"""

from collector.github import GitHubCollector
from intelligence.summarizer import RepositorySummarizer
from intelligence.analyzer import RepositoryAnalyzer
from intelligence.contributor import ContributorAdvisor


def main() -> None:
    collector = GitHubCollector()

    repository = collector.collect("https://github.com/psf/requests")

    issues = collector.collect_issues("https://github.com/psf/requests")

    summarizer = RepositorySummarizer()
    summary = summarizer.summarize(repository)

    analyzer = RepositoryAnalyzer()
    insights = analyzer.analyze(repository)

    advisor = ContributorAdvisor()
    advice = advisor.advise(repository)

    print("\nRepository collected successfully!\n")

    print(f"Name: {repository.name}")
    print(f"Owner: {repository.owner}")
    print(f"Language: {repository.language}")
    print(f"Description: {repository.description}")
    print(f"Default branch: {repository.default_branch}")
    print(f"License: {repository.license}")
    print(f"URL: {repository.url}")

    print("\nRepository Analysis")
    print("-------------------")

    for key, value in insights.items():
        print(f"{key}: {value}")

    print("\nContribution Advice")
    print("-------------------")

    for item in advice:
        print(f"- {item}")

    print("\nOpen Issues")
    print("-----------")

    for issue in issues[:5]:
        print(f"#{issue.number} - {issue.title}")

    print("\nSummary")
    print("-------")
    print(summary)


if __name__ == "__main__":
    main()
