"""
Example demonstrating ORI's first repository collection.

Run with:

    python examples/collect_repository.py
"""

from collector.github import GitHubCollector


def main() -> None:
    collector = GitHubCollector()

    repository = collector.collect(
        "https://github.com/psf/requests"
    )

    print("\nRepository collected successfully!\n")

    print(f"Name: {repository.name}")
    print(f"Owner: {repository.owner}")
    print(f"Description: {repository.description}")
    print(f"Default branch: {repository.default_branch}")
    print(f"License: {repository.license}")
    print(f"URL: {repository.url}")


if __name__ == "__main__":
    main()
