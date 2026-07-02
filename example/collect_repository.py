"""
Example demonstrating ORI's first repository collection.

Run with:

    python example/collect_repository.py
"""

from collector.github import GitHubCollector
from intelligence.summarizer import RepositorySummarizer


def main() -> None:
    collector = GitHubCollector()

    repository = collector.collect(
        "https://github.com/psf/requests"
    )

    summarizer = RepositorySummarizer()
    summary = summarizer.summarize(repository)

    print("\nRepository collected successfully!\n")

    print(f"Name: {repository.name}")
    print(f"Owner: {repository.owner}")
    print(f"Description: {repository.description}")
    print(f"Default branch: {repository.default_branch}")
    print(f"License: {repository.license}")
    print(f"URL: {repository.url}")

    print("\nSummary")
    print("-------")
    print(summary)


if __name__ == "__main__":
    main()