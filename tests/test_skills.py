"""
Tests for the Repository Skill Analyzer.
"""

from collector.types import RepositoryMetadata
from intelligence.skills import SkillAnalyzer


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


def test_python_repository_detects_expected_skills():
    analyzer = SkillAnalyzer()

    result = analyzer.analyze(make_repository())

    assert result.primary_language == "Python"
    assert "Python" in result.required_skills
    assert "Git" in result.required_skills
    assert "Virtual Environments" in result.required_skills


def test_frameworks_are_detected_from_readme():
    analyzer = SkillAnalyzer()

    readme = """
    Built with Django and FastAPI.
    """

    result = analyzer.analyze(
        make_repository(),
        readme,
    )

    assert "Django" in result.frameworks
    assert "FastAPI" in result.frameworks


def test_tools_are_detected_from_readme():
    analyzer = SkillAnalyzer()

    readme = """
    pip install ori

    pytest

    Docker

    GitHub Actions
    """

    result = analyzer.analyze(
        make_repository(),
        readme,
    )

    assert "pip" in result.recommended_tools
    assert "pytest" in result.recommended_tools
    assert "Docker" in result.recommended_tools
    assert "GitHub Actions" in result.recommended_tools


def test_unknown_language_defaults_to_git():
    analyzer = SkillAnalyzer()

    result = analyzer.analyze(
        make_repository(language="Elixir"),
    )

    assert "Elixir" in result.required_skills
    assert "Git" in result.required_skills


def test_large_repository_is_advanced():
    analyzer = SkillAnalyzer()

    result = analyzer.analyze(
        make_repository(stars=25000),
        "django flask fastapi",
    )

    assert result.difficulty == "Advanced"


def test_small_repository_is_beginner():
    analyzer = SkillAnalyzer()

    result = analyzer.analyze(
        make_repository(stars=25),
    )

    assert result.difficulty == "Beginner"