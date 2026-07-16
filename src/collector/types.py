"""
Data models used by the collector package.

These models represent raw repository information collected from supported
repository providers before they are transformed into Repository Intelligence.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryMetadata:
    """
    Basic metadata describing a repository.

    This model represents the raw information collected from a
    repository provider before intelligence analysis begins.
    """

    # ------------------------------------------------------------------
    # Core Repository Information
    # ------------------------------------------------------------------

    name: str
    owner: str
    url: str

    description: str | None = None
    default_branch: str | None = None
    license: str | None = None
    language: str | None = None

    # ------------------------------------------------------------------
    # Community Metrics
    # ------------------------------------------------------------------

    stars: int = 0
    forks: int = 0
    watchers: int = 0
    open_issues: int = 0

    # ------------------------------------------------------------------
    # Repository Status
    # ------------------------------------------------------------------

    archived: bool = False

    last_push: str | None = None
    last_update: str | None = None

    default_branch_protected: bool = False

    # ------------------------------------------------------------------
    # Governance Signals
    # ------------------------------------------------------------------

    has_contributing_guide: bool = False
    has_code_of_conduct: bool = False
    has_security_policy: bool = False
    has_issue_templates: bool = False
    has_pull_request_template: bool = False


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
