"""
Tests for the Developer Fit Analyzer.
"""

from collector.types import RepositoryMetadata
from intelligence.developer_fit import DeveloperFitAnalyzer
from intelligence.models import RepositoryDocumentation, SkillProfile


def make_repository(**overrides):
    """Create a repository with sensible defaults."""

    data = {
        "name": "ori",
        "owner": "oryke",
        "url": "https://github.com/Oryke/ori",
        "description": "Repository Intelligence",
        "language": "Python",
        "license": "MIT",
        "default_branch": "main",
        "stars": 500,
        "forks": 40,
        "watchers": 20,
        "open_issues": 10,
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


def make_documentation(**overrides):
    """Create documentation with sensible defaults."""

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


def make_skills(**overrides):
    """Create a skill profile."""

    data = {
        "primary_language": "Python",
        "difficulty": "Intermediate",
        "required_skills": ["Python", "Git"],
        "recommended_tools": ["Git"],
        "frameworks": [],
        "reasons": [],
    }

    data.update(overrides)
    return SkillProfile(**data)


def test_large_repository_requires_intermediate_to_advanced_experience():
    analyzer = DeveloperFitAnalyzer()

    result = analyzer.evaluate(
        make_repository(stars=25000),
        make_documentation(),
        make_skills(),
    )

    assert result.experience_level == "Intermediate to Advanced"


def test_small_repository_is_beginner_friendly():
    analyzer = DeveloperFitAnalyzer()

    result = analyzer.evaluate(
        make_repository(stars=50),
        make_documentation(),
        make_skills(),
    )

    assert result.experience_level == "Beginner Friendly"


def test_advanced_projects_have_longer_onboarding():
    analyzer = DeveloperFitAnalyzer()

    result = analyzer.evaluate(
        make_repository(),
        make_documentation(),
        make_skills(difficulty="Advanced"),
    )

    assert result.estimated_onboarding == "2-4 weeks"


def test_open_issues_are_recommended_for_contribution():
    analyzer = DeveloperFitAnalyzer()

    result = analyzer.evaluate(
        make_repository(open_issues=15),
        make_documentation(),
        make_skills(),
    )

    assert "Review and resolve open issues" in result.recommended_contributions


def test_missing_contributing_guide_is_reported():
    analyzer = DeveloperFitAnalyzer()

    result = analyzer.evaluate(
        make_repository(),
        make_documentation(has_contributing_guide=False),
        make_skills(),
    )

    assert any(
        "Missing contribution documentation" in reason
        for reason in result.reasons
    )


def test_confidence_reaches_full_score_with_complete_information():
    analyzer = DeveloperFitAnalyzer()

    result = analyzer.evaluate(
        make_repository(),
        make_documentation(),
        make_skills(),
    )

    assert result.confidence == 100