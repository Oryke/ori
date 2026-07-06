"""
Data models used by the collector package.

These models represent raw repository information collected from supported
repository providers before it is transformed into Repository Intelligence.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class RepositoryMetadata:
    """
    Basic metadata describing a repository.

    This model represents the first layer of information collected by ORI.
    It intentionally contains only high-level repository details.
    """

    name: str
    owner: str
    url: str

    description: str | None = None
    default_branch: str | None = None
    license: str | None = None
    language: str | None = None

    stars: int = 0
    forks: int = 0
    watchers: int = 0
    open_issues: int = 0


@dataclass(slots=True)
class IssueMetadata:
    """
    Basic metadata describing a GitHub issue.
    """

    number: int
    title: str
    url: str

    labels: list[str]
    state: str