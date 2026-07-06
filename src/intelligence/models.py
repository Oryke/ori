from dataclasses import dataclass, field


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
    Represents ORI's overall health evaluation of a repository.
    """

    overall_score: int
    overall_rating: str
    overall_reasons: list[str] = field(default_factory=list)

    community: HealthDimension | None = None
    maintenance: HealthDimension | None = None
    governance: HealthDimension | None = None