"""
Example demonstrating how to collect repository metadata.

Run with:

    python examples/collect_repository.py
"""

import httpx

from src.collector.github import GitHubCollector


def main() -> None:
    """Collect and display metadata for a public GitHub repository."""

    collector = GitHubCollector()

    repository_url = "https://github.com/openai/openai-python"

    try:
        repository = collector.collect(repository_url)

    except ValueError as error:
        print(f"Invalid repository: {error}")

    except httpx.HTTPStatusError as error:
        print(f"GitHub API returned an error: {error}")

    except httpx.RequestError as error:
        print(f"Unable to connect to GitHub: {error}")

    else:
        print("Repository Information")
        print("----------------------")
        print(f"Name: {repository.name}")
        print(f"Owner: {repository.owner}")
        print(f"Description: {repository.description}")
        print(f"Default Branch: {repository.default_branch}")
        print(f"License: {repository.license}")
        print(f"URL: {repository.url}")


if __name__ == "__main__":
    main()
