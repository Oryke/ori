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