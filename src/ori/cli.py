"""
ORI Command Line Interface.

The primary entry point into ORI.
"""

import argparse

from collector.documentation import DocumentationCollector
from collector.github import GitHubCollector

from intelligence.analyzer import RepositoryAnalyzer
from intelligence.contributor import ContributorAdvisor
from intelligence.documentation import DocumentationAnalyzer
from intelligence.developer_fit import DeveloperFitAnalyzer
from intelligence.evaluation import RepositoryEvaluator
from intelligence.health import RepositoryHealthEngine
from intelligence.risk import RepositoryRiskAnalyzer
from intelligence.roadmap import RoadmapAnalyzer
from intelligence.skills import SkillAnalyzer
from intelligence.summarizer import RepositorySummarizer
from ori.reporter import RepositoryReporter


VERSION = "1.0.0"


def analyze_repository(url: str) -> str:
    """
    Analyze a repository and generate an ORI report.
    """

    collector = GitHubCollector()
    documentation_collector = DocumentationCollector()

    repository = collector.collect(url)
    issues = collector.collect_issues(url)
    readme = documentation_collector.collect_readme(url)

    analyzer = RepositoryAnalyzer()
    insights = analyzer.analyze(repository)

    advisor = ContributorAdvisor()
    advice = advisor.advise(repository)

    health = RepositoryHealthEngine().evaluate(repository)

    documentation = DocumentationAnalyzer().analyze(readme)

    risk = RepositoryRiskAnalyzer().evaluate(
        repository,
        documentation,
    )

    skills = SkillAnalyzer().analyze(
        repository,
        readme,
    )

    developer_fit = DeveloperFitAnalyzer().evaluate(
        repository,
        documentation,
        skills,
    )

    roadmap = RoadmapAnalyzer().generate(
        repository,
        health,
        documentation,
        risk,
        skills,
        developer_fit,
    )

    evaluation = RepositoryEvaluator().evaluate(
        health=health,
        documentation=documentation,
        risk=risk,
        skills=skills,
        developer_fit=developer_fit,
        roadmap=roadmap,
    )

    summary = RepositorySummarizer().summarize(repository)

    report = RepositoryReporter().generate(
        repository=repository,
        summary=summary,
        health=health,
        documentation=documentation,
        risk=risk,
        skills=skills,
        developer_fit=developer_fit,
        roadmap=roadmap,
        evaluation=evaluation,
        insights=insights,
        advice=advice,
        issues=issues,
    )

    return report


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="ori",
        description="ORI - Repository Intelligence Engine"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"ORI {VERSION}",
    )

    parser.add_argument(
        "repository",
        nargs="?",
        help="GitHub repository URL to analyze",
    )

    args = parser.parse_args()

    if not args.repository:
        parser.print_help()
        return

    report = analyze_repository(args.repository)

    print(report)


if __name__ == "__main__":
    main()