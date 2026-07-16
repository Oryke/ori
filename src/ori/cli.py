"""
ORI Command Line Interface.

The primary entry point into ORI.
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


def main() -> None:
    url = input("Repository URL: ")

    # ---------------------------------------------------------------
    # Collect Repository Data
    # ---------------------------------------------------------------

    collector = GitHubCollector()
    documentation_collector = DocumentationCollector()

    repository = collector.collect(url)
    issues = collector.collect_issues(url)
    readme = documentation_collector.collect_readme(url)

    # ---------------------------------------------------------------
    # Intelligence Engines
    # ---------------------------------------------------------------

    analyzer = RepositoryAnalyzer()
    insights = analyzer.analyze(repository)

    advisor = ContributorAdvisor()
    advice = advisor.advise(repository)

    health_engine = RepositoryHealthEngine()
    health = health_engine.evaluate(repository)

    documentation_analyzer = DocumentationAnalyzer()
    documentation = documentation_analyzer.analyze(readme)

    risk_analyzer = RepositoryRiskAnalyzer()

    risk = risk_analyzer.evaluate(
        repository,
        documentation,
    )

    skill_analyzer = SkillAnalyzer()

    skills = skill_analyzer.analyze(
        repository,
        readme,
    )

    developer_fit_analyzer = DeveloperFitAnalyzer()

    developer_fit = developer_fit_analyzer.evaluate(
        repository,
        documentation,
        skills,
    )

    roadmap_analyzer = RoadmapAnalyzer()

    roadmap = roadmap_analyzer.generate(
        repository,
        health,
        documentation,
        risk,
        skills,
        developer_fit,
    )

    evaluator = RepositoryEvaluator()

    evaluation = evaluator.evaluate(
        health=health,
        documentation=documentation,
        risk=risk,
        skills=skills,
        developer_fit=developer_fit,
        roadmap=roadmap,
    )

    summarizer = RepositorySummarizer()
    summary = summarizer.summarize(repository)

    report_generator = RepositoryReporter()

    report = report_generator.generate(
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


if __name__ == "__main__":
    main()
