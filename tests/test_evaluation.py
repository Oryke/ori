"""
Tests for ORI Repository Evaluation Engine.
"""

from intelligence.evaluation import RepositoryEvaluator
from intelligence.models import (
    RepositoryHealth,
    HealthDimension,
    RepositoryDocumentation,
    RepositoryRisk,
)


def create_health(score: int = 90) -> RepositoryHealth:
    """Create a sample repository health object."""

    return RepositoryHealth(
        overall_score=score,
        overall_rating="★★★★★ Excellent",
        overall_reasons=[],
        community=HealthDimension(
            score=95,
            rating="Excellent",
            reasons=[],
        ),
        maintenance=HealthDimension(
            score=90,
            rating="Excellent",
            reasons=[],
        ),
        governance=HealthDimension(
            score=85,
            rating="Good",
            reasons=[],
        ),
    )


def create_documentation(
    readme: bool = True,
    installation: bool = True,
    usage: bool = True,
    contributing: bool = True,
) -> RepositoryDocumentation:
    """Create sample documentation analysis."""

    return RepositoryDocumentation(
        has_readme=readme,
        has_installation=installation,
        has_usage_examples=usage,
        has_contributing_guide=contributing,
        has_api_documentation=False,
        has_license_section=True,
        beginner_friendly=True,
        summary="Documentation looks good.",
    )


def create_risk(score: int = 95) -> RepositoryRisk:
    """Create a sample repository risk assessment."""

    return RepositoryRisk(
        score=score,
        level="VERY LOW",
        reasons=[],
        warnings=[],
        recommendation="Excellent candidate.",
    )


def test_high_quality_repository_scores_well():
    """Healthy repositories should receive a high evaluation score."""

    evaluator = RepositoryEvaluator()

    result = evaluator.evaluate(
        health=create_health(),
        documentation=create_documentation(),
        risk=create_risk(),
    )

    assert result.overall_score >= 70
    assert "Repository demonstrates strong overall health." in result.strengths
    assert result.confidence >= 80
    assert result.overall_rating in (
        "★★★★★ Excellent",
        "★★★★☆ Good",
    )


def test_missing_readme_is_reported():
    """Repositories without a README should report a weakness."""

    evaluator = RepositoryEvaluator()

    result = evaluator.evaluate(
        health=create_health(),
        documentation=create_documentation(readme=False),
        risk=create_risk(),
    )

    assert "Repository is missing a README." in result.weaknesses


def test_missing_contributing_guide_adds_insight():
    """Missing contribution guide should generate an onboarding insight."""

    evaluator = RepositoryEvaluator()

    result = evaluator.evaluate(
        health=create_health(),
        documentation=create_documentation(contributing=False),
        risk=create_risk(),
    )

    assert (
        "Missing contributor documentation may increase onboarding difficulty."
        in result.insights
    )


def test_low_risk_repository_is_recognized():
    """Repositories with low risk should be identified correctly."""

    evaluator = RepositoryEvaluator()

    result = evaluator.evaluate(
        health=create_health(),
        documentation=create_documentation(),
        risk=create_risk(score=95),
    )

    assert "Repository presents low adoption risk." in result.strengths


def test_high_health_repositories_are_recommended_for_production():
    """Healthy repositories should be recommended for production use."""

    evaluator = RepositoryEvaluator()

    result = evaluator.evaluate(
        health=create_health(score=90),
        documentation=create_documentation(),
        risk=create_risk(),
    )

    assert "Production use" in result.recommended_for
    assert "Open-source contribution" in result.recommended_for
