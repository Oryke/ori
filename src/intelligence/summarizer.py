from collector.types import RepositoryMetadata


class RepositorySummarizer:
    """Generate a simple natural-language summary of a repository."""

    def summarize(self, repository: RepositoryMetadata) -> str:
        return (
            f"{repository.owner}/{repository.name} "
            f"is a GitHub repository whose default branch is "
            f"'{repository.default_branch}'. "
            f"It is licensed under {repository.license}. "
            f"Description: {repository.description}"
        )