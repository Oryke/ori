"""
ORI Contributor Roadmap Intelligence.

Generates a contribution journey for developers
based on repository maturity, documentation,
skills, health, risk, and contributor readiness.
"""

from intelligence.models import ContributorRoadmap


class RoadmapAnalyzer:
    """
    Generates contributor roadmaps.
    """

    def generate(
        self,
        repository,
        health,
        documentation,
        risk,
        skills,
        developer_fit,
    ) -> ContributorRoadmap:
        """
        Create a personalized contribution roadmap.
        """

        next_steps: list[str] = []

        contribution_opportunities: list[str] = []

        reasons: list[str] = []


        # ------------------------------------------------------------
        # Determine contributor stage
        # ------------------------------------------------------------

        experience = developer_fit.experience_level


        if "Beginner" in experience:

            current_stage = "Beginner Contributor"

            recommended_focus = (
                "Learn the repository structure, "
                "understand contribution workflows, "
                "and start with low-risk improvements."
            )


            next_steps.extend(
                [
                    "Read the README and project documentation.",
                    "Set up the development environment locally.",
                    "Understand the repository folder structure.",
                    "Start with documentation or beginner-friendly issues.",
                ]
            )


            contribution_opportunities.extend(
                [
                    "Documentation improvements",
                    "Example updates",
                    "Test coverage improvements",
                    "Issue discussions",
                ]
            )


        elif "Intermediate" in experience:

            current_stage = "Intermediate Contributor"

            recommended_focus = (
                "Contribute meaningful fixes, "
                "improve existing features, "
                "and collaborate with maintainers."
            )


            next_steps.extend(
                [
                    "Study the repository architecture.",
                    "Review active issues and pull requests.",
                    "Identify bugs or improvement opportunities.",
                    "Submit small focused pull requests.",
                ]
            )


            contribution_opportunities.extend(
                [
                    "Bug fixes",
                    "Feature improvements",
                    "Testing improvements",
                    "Code reviews",
                ]
            )


        else:

            current_stage = "Advanced Contributor"

            recommended_focus = (
                "Drive technical improvements, "
                "architecture discussions, "
                "and major contributions."
            )


            next_steps.extend(
                [
                    "Analyze core architecture decisions.",
                    "Review roadmap and long-term issues.",
                    "Propose technical improvements.",
                    "Mentor newer contributors.",
                ]
            )


            contribution_opportunities.extend(
                [
                    "Major feature development",
                    "Architecture improvements",
                    "Performance optimization",
                    "Maintainer collaboration",
                ]
            )



        # ------------------------------------------------------------
        # Documentation Intelligence
        # ------------------------------------------------------------

        if documentation.has_readme:

            reasons.append(
                "Repository documentation provides an entry point for contributors."
            )

        else:

            next_steps.insert(
                0,
                "Create or improve repository documentation before contributing code."
            )



        if not documentation.has_contributing_guide:

            reasons.append(
                "Missing contribution guidelines increase onboarding difficulty."
            )

            next_steps.append(
                "Review existing pull requests to understand contribution standards."
            )



        # ------------------------------------------------------------
        # Health Intelligence
        # ------------------------------------------------------------

        if health.overall_score >= 80:

            reasons.append(
                "Strong repository health suggests an active contribution environment."
            )

        else:

            next_steps.append(
                "Review repository maintenance activity before making major contributions."
            )



        # ------------------------------------------------------------
        # Risk Intelligence
        # ------------------------------------------------------------

        if risk.level == "LOW":

            reasons.append(
                "Low repository risk indicates a stable project to contribute to."
            )

        else:

            next_steps.append(
                "Review repository risks before investing significant contribution effort."
            )



        # ------------------------------------------------------------
        # Skill Intelligence
        # ------------------------------------------------------------

        if skills.required_skills:

            next_steps.append(
                "Build confidence with required skills: "
                + ", ".join(skills.required_skills[:3])
            )


        # ------------------------------------------------------------
        # Adoption Intelligence
        # ------------------------------------------------------------

        if repository.stars >= 10000:

            reasons.append(
                "High community adoption indicates established project practices."
            )

            contribution_opportunities.append(
                "Community participation"
            )



        return ContributorRoadmap(

            current_stage=current_stage,

            recommended_focus=recommended_focus,

            next_steps=next_steps,

            contribution_opportunities=(
                contribution_opportunities
            ),

            reasons=reasons,

        )