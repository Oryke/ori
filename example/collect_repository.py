"""
Example demonstrating ORI's first repository collection.

Run with:

    python example/collect_repository.py
"""

from collector.github import GitHubCollector
from intelligence.summarizer import RepositorySummarizer
from intelligence.analyzer import RepositoryAnalyzer


def main() -> None:
    collector = GitHubCollector()

    repository = collector.collect(
        "https://github.com/psf/requests"
    )

    analyzer = RepositoryAnalyzer()
    insights = analyzer.analyze(repository)

    summarizer = RepositorySummarizer()
    summary = summarizer.summarize(repository)

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

    print("\nSummary")
    print("-------")
    print(summary)


if __name__ == "__main__":
    main()