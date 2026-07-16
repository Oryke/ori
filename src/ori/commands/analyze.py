"""
ORI Analyze Command.

Runs full repository intelligence analysis.
"""

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


def run(repository_url: str) -> None:
    """
    Execute complete ORI repository analysis.
    """

    # ---------------------------------------------------------------
    # Collect repository data
    # ---------------------------------------------------------------

    collector = GitHubCollector()
    documentation_collector = DocumentationCollector()

    repository = collector.collect(repository_url)
    issues = collector.collect_issues(repository_url)
    readme = documentation_collector.collect_readme(repository_url)

    # ---------------------------------------------------------------
    # Run intelligence engines
    # ---------------------------------------------------------------

    insights = RepositoryAnalyzer().analyze(repository)

    advice = ContributorAdvisor().advise(repository)

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

    # ---------------------------------------------------------------
    # Generate report
    # ---------------------------------------------------------------

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

    print(report)