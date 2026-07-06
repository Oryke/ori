"""
Core intelligence models used throughout ORI.

These models represent the structured intelligence produced by
ORI's analysis engines.
"""

from dataclasses import dataclass, field


# ---------------------------------------------------------------------
# Repository Health
# ---------------------------------------------------------------------

@dataclass
class HealthDimension:
    """
    Represents the evaluation of a single repository health dimension.
    """

    score: int
    rating: str
    reasons: list[str] = field(default_factory=list)


@dataclass
class RepositoryHealth:
    """
    Represents ORI's overall repository health evaluation.
    """

    overall_score: int
    overall_rating: str
    overall_reasons: list[str] = field(default_factory=list)

    community: HealthDimension | None = None
    maintenance: HealthDimension | None = None
    governance: HealthDimension | None = None


# ---------------------------------------------------------------------
# Repository Documentation
# ---------------------------------------------------------------------

@dataclass
class RepositoryDocumentation:
    """
    Represents ORI's documentation analysis for a repository.
    """

    has_readme: bool = False

    has_installation: bool = False

    has_usage_examples: bool = False

    has_contributing_guide: bool = False

    has_api_documentation: bool = False

    has_license_section: bool = False

    beginner_friendly: bool = False

    summary: str = ""