"""
Core intelligence models used throughout ORI.

These models represent the structured intelligence produced by
ORI's analysis engines.
"""

from dataclasses import dataclass, field


# ---------------------------------------------------------------------
# Analysis Metadata
# ---------------------------------------------------------------------

@dataclass(slots=True)
class AnalysisMetadata:
    """
    Metadata about an ORI analysis run.
    """

    generated_at: str = ""

    analyzer_version: str = "0.1.0"


# ---------------------------------------------------------------------
# Repository Health
# ---------------------------------------------------------------------

@dataclass(slots=True)
class HealthDimension:
    """
    Represents the evaluation of a single repository health dimension.
    """

    score: int
    rating: str
    reasons: list[str] = field(default_factory=list)


@dataclass(slots=True)
class RepositoryHealth:
    """
    Represents ORI's overall repository health evaluation.
    """

    overall_score: int

    overall_rating: str

    overall_reasons: list[str] = field(
        default_factory=list
    )

    community: HealthDimension | None = None

    maintenance: HealthDimension | None = None

    governance: HealthDimension | None = None


# ---------------------------------------------------------------------
# Repository Documentation
# ---------------------------------------------------------------------

@dataclass(slots=True)
class RepositoryDocumentation:
    """
    Represents ORI's documentation analysis.
    """

    has_readme: bool = False
    has_installation: bool = False
    has_usage_examples: bool = False
    has_contributing_guide: bool = False
    has_api_documentation: bool = False
    has_license_section: bool = False
    beginner_friendly: bool = False

    summary: str = ""


# ---------------------------------------------------------------------
# Repository Risk
# ---------------------------------------------------------------------

@dataclass(slots=True)
class RepositoryRisk:
    """
    Represents ORI's assessment of repository risk.
    """

    score: int
    level: str

    reasons: list[str] = field(
        default_factory=list
    )

    warnings: list[str] = field(
        default_factory=list
    )

    recommendation: str = ""


# ---------------------------------------------------------------------
# Repository Skills
# ---------------------------------------------------------------------

@dataclass(slots=True)
class SkillProfile:
    """
    Represents the technical skills required to contribute
    to a repository.
    """

    primary_language: str = ""

    difficulty: str = "Unknown"

    required_skills: list[str] = field(
        default_factory=list
    )

    recommended_tools: list[str] = field(
        default_factory=list
    )

    frameworks: list[str] = field(
        default_factory=list
    )

    reasons: list[str] = field(
        default_factory=list
    )


# ---------------------------------------------------------------------
# Developer Fit
# ---------------------------------------------------------------------

@dataclass(slots=True)
class DeveloperFit:
    """
    Represents ORI's assessment of contributor suitability.

    Determines how suitable a repository is for a developer
    based on experience level, onboarding difficulty,
    required skills, and contribution opportunities.
    """

    experience_level: str = "Unknown"

    estimated_onboarding: str = "Unknown"

    confidence: int = 0

    recommended_skills: list[str] = field(
        default_factory=list
    )

    recommended_contributions: list[str] = field(
        default_factory=list
    )

    reasons: list[str] = field(
        default_factory=list
    )


# ---------------------------------------------------------------------
# Contributor Roadmap
# ---------------------------------------------------------------------

@dataclass(slots=True)
class ContributorRoadmap:
    """
    Represents ORI's personalized contributor roadmap.

    Guides contributors through the most appropriate
    contribution path based on repository maturity
    and developer readiness.
    """

    current_stage: str = "Unknown"

    recommended_focus: str = ""

    next_steps: list[str] = field(
        default_factory=list
    )

    contribution_opportunities: list[str] = field(
        default_factory=list
    )

    reasons: list[str] = field(
        default_factory=list
    )


# ---------------------------------------------------------------------
# Repository Evaluation
# ---------------------------------------------------------------------

@dataclass(slots=True)
class RepositoryEvaluation:
    """
    Represents ORI's complete repository intelligence report.
    """

    overall_score: int

    overall_rating: str

    metadata: AnalysisMetadata = field(
        default_factory=AnalysisMetadata
    )

    confidence: int = 0

    strengths: list[str] = field(
        default_factory=list
    )

    weaknesses: list[str] = field(
        default_factory=list
    )

    recommended_for: list[str] = field(
        default_factory=list
    )

    insights: list[str] = field(
        default_factory=list
    )

    health: RepositoryHealth | None = None

    documentation: RepositoryDocumentation | None = None

    risk: RepositoryRisk | None = None

    skills: SkillProfile | None = None

    developer_fit: DeveloperFit | None = None

    roadmap: ContributorRoadmap | None = None