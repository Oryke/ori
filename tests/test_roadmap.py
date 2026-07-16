"""
Tests for the Roadmap Analyzer.
"""

from collector.types import RepositoryMetadata
from intelligence.models import (
    DeveloperFit,
    RepositoryDocumentation,
    RepositoryHealth,
    RepositoryRisk,
    SkillProfile,
)
from intelligence.roadmap import RoadmapAnalyzer


def make_repository(**overrides):
    data = {
        "name": "ori",
        "owner": "oryke",
        "url": "https://github.com/Oryke/ori",
        "description": "Repository Intelligence",
        "language": "Python",
        "license": "MIT",
        "default_branch": "main",
        "stars": 500,
        "forks": 50,
        "watchers": 20,
        "open_issues": 15,
        "archived": False,
        "last_push": "2026-07-01T00:00:00Z",
        "has_security_policy": True,
        "has_code_of_conduct": True,
        "has_contributing_guide": True,
        "has_issue_templates": True,
        "has_pull_request_template": True,
    }

    data.update(overrides)
    return RepositoryMetadata(**data)


def make_health(score=90):
    return RepositoryHealth(
        overall_score=score,
        overall_rating="Excellent",
    )


def make_documentation(**overrides):
    data = {
        "has_readme": True,
        "has_installation": True,
        "has_usage_examples": True,
        "has_contributing_guide": True,
        "has_api_documentation": False,
        "has_license_section": True,
        "beginner_friendly": False,
        "summary": "",
    }

    data.update(overrides)
    return RepositoryDocumentation(**data)


def make_risk(level="LOW"):
    return RepositoryRisk(
        score=90,
        level=level,
    )


def make_skills():
    return SkillProfile(
        primary_language="Python",
        difficulty="Intermediate",
        required_skills=["Python", "Git", "pytest"],
    )


def make_developer_fit(level="Intermediate"):
    return DeveloperFit(
        experience_level=level,
        estimated_onboarding="1-2 weeks",
        confidence=90,
    )


def test_beginner_repository_generates_beginner_roadmap():
    analyzer = RoadmapAnalyzer()

    roadmap = analyzer.generate(
        make_repository(),
        make_health(),
        make_documentation(),
        make_risk(),
        make_skills(),
        make_developer_fit("Beginner Friendly"),
    )

    assert roadmap.current_stage == "Beginner Contributor"


def test_intermediate_repository_generates_intermediate_roadmap():
    analyzer = RoadmapAnalyzer()

    roadmap = analyzer.generate(
        make_repository(),
        make_health(),
        make_documentation(),
        make_risk(),
        make_skills(),
        make_developer_fit("Intermediate"),
    )

    assert roadmap.current_stage == "Intermediate Contributor"


def test_advanced_repository_generates_advanced_roadmap():
    analyzer = RoadmapAnalyzer()

    roadmap = analyzer.generate(
        make_repository(),
        make_health(),
        make_documentation(),
        make_risk(),
        make_skills(),
        make_developer_fit("Advanced"),
    )

    assert roadmap.current_stage == "Advanced Contributor"


def test_missing_contributing_guide_adds_extra_step():
    analyzer = RoadmapAnalyzer()

    roadmap = analyzer.generate(
        make_repository(),
        make_health(),
        make_documentation(has_contributing_guide=False),
        make_risk(),
        make_skills(),
        make_developer_fit(),
    )

    assert any(
        "Review existing pull requests" in step
        for step in roadmap.next_steps
    )


def test_high_star_repository_encourages_community_participation():
    analyzer = RoadmapAnalyzer()

    roadmap = analyzer.generate(
        make_repository(stars=25000),
        make_health(),
        make_documentation(),
        make_risk(),
        make_skills(),
        make_developer_fit(),
    )

    assert "Community participation" in roadmap.contribution_opportunities


def test_required_skills_are_added_to_next_steps():
    analyzer = RoadmapAnalyzer()

    roadmap = analyzer.generate(
        make_repository(),
        make_health(),
        make_documentation(),
        make_risk(),
        make_skills(),
        make_developer_fit(),
    )

    assert any(
        "Build confidence with required skills" in step
        for step in roadmap.next_steps
    )