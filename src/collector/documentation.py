"""
Documentation Collector.

Collects repository documentation from supported providers.
"""

from collector.github import GitHubCollector


class DocumentationCollector:
    """
    Collects repository documentation.
    """

    def __init__(self) -> None:
        self.github = GitHubCollector()

    def collect_readme(self, repository_url: str) -> str:
        """
        Return the repository README as plain text.
        """
        return self.github.collect_readme(repository_url)
