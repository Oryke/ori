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



    # ---------------------------------------------------------------
    # ORI Report
    # ---------------------------------------------------------------


    print("\nORI Analysis")
    print("=" * 40)


    print(
        f"\nRepository: "
        f"{repository.owner}/{repository.name}"
    )

    print(
        f"Language: "
        f"{repository.language}"
    )

    print(
        f"License: "
        f"{repository.license}"
    )

    print(
        f"Default Branch: "
        f"{repository.default_branch}"
    )

    print(
        f"URL: "
        f"{repository.url}"
    )


    # ---------------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------------


    print("\nRepository Statistics")
    print("---------------------")

    print(f"Stars: {repository.stars}")
    print(f"Forks: {repository.forks}")
    print(f"Watchers: {repository.watchers}")
    print(f"Open Issues: {repository.open_issues}")



    # ---------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------


    print("\nSummary")
    print("-------")

    print(summary)



    # ---------------------------------------------------------------
    # Health
    # ---------------------------------------------------------------


    print("\nRepository Health")
    print("-----------------")


    print("\nOverall")

    print(
        f"  Score : "
        f"{health.overall_score}/100"
    )

    print(
        f"  Rating: "
        f"{health.overall_rating}"
    )


    for reason in health.overall_reasons:
        print(f"    • {reason}")


    for name, dimension in [
        ("Community", health.community),
        ("Maintenance", health.maintenance),
        ("Governance", health.governance),
    ]:

        print(f"\n{name}")

        print(
            f"  Score : "
            f"{dimension.score}/100"
        )

        print(
            f"  Rating: "
            f"{dimension.rating}"
        )


        for reason in dimension.reasons:
            print(f"    • {reason}")



    # ---------------------------------------------------------------
    # Documentation
    # ---------------------------------------------------------------


    print("\nDocumentation")
    print("-------------")


    print(
        f"README: "
        f"{'Yes' if documentation.has_readme else 'No'}"
    )

    print(
        f"Installation Guide: "
        f"{'Yes' if documentation.has_installation else 'No'}"
    )

    print(
        f"Usage Examples: "
        f"{'Yes' if documentation.has_usage_examples else 'No'}"
    )

    print(
        f"Contributing Guide: "
        f"{'Yes' if documentation.has_contributing_guide else 'No'}"
    )

    print(
        f"API Documentation: "
        f"{'Yes' if documentation.has_api_documentation else 'No'}"
    )

    print(
        f"License Section: "
        f"{'Yes' if documentation.has_license_section else 'No'}"
    )

    print(
        f"Beginner Friendly: "
        f"{'Yes' if documentation.beginner_friendly else 'No'}"
    )


    print("\nSummary")

    print(
        f"  {documentation.summary}"
    )



    # ---------------------------------------------------------------
    # Risk
    # ---------------------------------------------------------------


    print("\nRepository Risk")
    print("----------------")


    print(
        f"Score : "
        f"{risk.score}/100"
    )

    print(
        f"Level : "
        f"{risk.level}"
    )


    print("\nReasons")

    for reason in risk.reasons:
        print(f"  ✓ {reason}")


    print("\nWarnings")

    for warning in risk.warnings:
        print(f"  ⚠ {warning}")


    print("\nRecommendation")

    print(
        f"  {risk.recommendation}"
    )



    # ---------------------------------------------------------------
    # Skills
    # ---------------------------------------------------------------


    print("\nDeveloper Skills")
    print("----------------")

    print(
        f"Primary Language: "
        f"{skills.primary_language}"
    )

    print(
        f"Difficulty: "
        f"{skills.difficulty}"
    )

    print("\nRequired Skills")

    for skill in skills.required_skills:
        print(f"  ✓ {skill}")

    print("\nFrameworks")

    if skills.frameworks:

        for framework in skills.frameworks:
            print(f"  ✓ {framework}")

    else:
        print("  None detected.")

    print("\nRecommended Tools")

    for tool in skills.recommended_tools:
        print(f"  ✓ {tool}")



    # ---------------------------------------------------------------
    # Developer Fit
    # ---------------------------------------------------------------


    print("\nDeveloper Fit")
    print("----------------")


    print(
        f"Experience Level: "
        f"{developer_fit.experience_level}"
    )

    print(
        f"Estimated Onboarding: "
        f"{developer_fit.estimated_onboarding}"
    )

    print(
        f"Confidence: "
        f"{developer_fit.confidence}%"
    )


    print("\nRecommended Contributions")

    for item in developer_fit.recommended_contributions:
        print(f"  ✓ {item}")


    print("\nReasons")

    for reason in developer_fit.reasons:
        print(f"  • {reason}")



    # ---------------------------------------------------------------
    # Roadmap
    # ---------------------------------------------------------------


    print("\nContribution Roadmap")
    print("--------------------")


    print(
        f"Current Stage: "
        f"{roadmap.current_stage}"
    )

    print(
        f"Recommended Focus: "
        f"{roadmap.recommended_focus}"
    )


    print("\nNext Steps")

    for step in roadmap.next_steps:
        print(f"  → {step}")


    print("\nContribution Opportunities")

    for item in roadmap.contribution_opportunities:
        print(f"  ✓ {item}")



    # ---------------------------------------------------------------
    # Evaluation
    # ---------------------------------------------------------------


    print("\nRepository Evaluation")
    print("---------------------")


    print(
        f"Overall Score : "
        f"{evaluation.overall_score}/100"
    )

    print(
        f"Overall Rating: "
        f"{evaluation.overall_rating}"
    )


    print("\nStrengths")

    for item in evaluation.strengths:
        print(f"  ✓ {item}")


    print("\nWeaknesses")

    for item in evaluation.weaknesses:
        print(f"  • {item}")


    print("\nRecommended For")

    for item in evaluation.recommended_for:
        print(f"  ✓ {item}")



    # ---------------------------------------------------------------
    # Insights
    # ---------------------------------------------------------------


    print("\nInsights")
    print("--------")


    for key, value in insights.items():
        print(
            f"- {key}: {value}"
        )



    # ---------------------------------------------------------------
    # Advice
    # ---------------------------------------------------------------


    print("\nAdvice")
    print("------")


    for item in advice:
        print(
            f"- {item}"
        )



    # ---------------------------------------------------------------
    # Issues
    # ---------------------------------------------------------------


    print("\nOpen Issues")
    print("-----------")


    for issue in issues[:5]:
        print(
            f"#{issue.number} - {issue.title}"
        )



if __name__ == "__main__":
    main()