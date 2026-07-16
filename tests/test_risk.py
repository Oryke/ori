"""
Tests for the Repository Risk Analyzer.
"""

from intelligence.documentation import DocumentationAnalyzer
from intelligence.risk import RepositoryRiskAnalyzer
from collector.types import RepositoryMetadata


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
        "stars": 250,
        "forks": 40,
        "watchers": 30,
        "open_issues": 20,
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


def documentation():
    """Return a well-documented repository."""

    return DocumentationAnalyzer().analyze(
        """
        # ORI

        ## Installation
        pip install ori

        ## Usage
        python -m ori.cli
        """
    )


def test_low_risk_repository_scores_high():
    analyzer = RepositoryRiskAnalyzer()

    result = analyzer.evaluate(
        make_repository(),
        documentation(),
    )

    assert result.score >= 90
    assert result.level == "VERY LOW"


def test_archived_repository_increases_risk():
    analyzer = RepositoryRiskAnalyzer()

    result = analyzer.evaluate(
        make_repository(archived=True),
        documentation(),
    )

    assert result.score < 100
    assert "Repository has been archived." in result.warnings


def test_missing_license_is_reported():
    analyzer = RepositoryRiskAnalyzer()

    result = analyzer.evaluate(
        make_repository(license=""),
        documentation(),
    )

    assert "Repository does not define a license." in result.warnings


def test_missing_security_policy_is_reported():
    analyzer = RepositoryRiskAnalyzer()

    result = analyzer.evaluate(
        make_repository(has_security_policy=False),
        documentation(),
    )

    assert "Missing SECURITY.md." in result.warnings


def test_large_number_of_open_issues_generates_warning():
    analyzer = RepositoryRiskAnalyzer()

    result = analyzer.evaluate(
        make_repository(open_issues=800),
        documentation(),
    )

    assert "Large number of open issues." in result.warnings


def test_missing_installation_and_usage_are_reported():
    analyzer = RepositoryRiskAnalyzer()

    poor_docs = DocumentationAnalyzer().analyze("# Empty README")

    result = analyzer.evaluate(
        make_repository(),
        poor_docs,
    )

    assert "Installation instructions missing." in result.warnings
    assert "Usage examples missing." in result.warnings