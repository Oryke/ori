"""
Repository Skill Intelligence.

Analyzes repository metadata and documentation to determine
the technical skills required to contribute successfully.
"""

from collector.types import RepositoryMetadata
from intelligence.models import SkillProfile


class SkillAnalyzer:
    """
    Determines the skills required for contributing to a repository.
    """

    LANGUAGE_SKILLS = {
        "Python": [
            "Python",
            "Git",
            "Virtual Environments",
            "Package Management",
        ],
        "JavaScript": [
            "JavaScript",
            "Git",
            "Node.js",
            "npm",
        ],
        "TypeScript": [
            "TypeScript",
            "JavaScript",
            "Node.js",
            "npm",
        ],
        "Go": [
            "Go",
            "Git",
            "Go Modules",
        ],
        "Rust": [
            "Rust",
            "Cargo",
            "Git",
        ],
        "Java": [
            "Java",
            "Git",
            "Maven",
        ],
        "C#": [
            "C#",
            ".NET",
            "Git",
        ],
    }

    FRAMEWORK_KEYWORDS = {
        "Django": ["django"],
        "Flask": ["flask"],
        "FastAPI": ["fastapi"],
        "React": ["react"],
        "Vue": ["vue"],
        "Angular": ["angular"],
        "Next.js": ["next.js", "nextjs"],
        "Express": ["express"],
        "Spring Boot": ["spring boot"],
        "TensorFlow": ["tensorflow"],
        "PyTorch": ["pytorch"],
    }

    TOOL_KEYWORDS = {
        "Docker": ["docker"],
        "GitHub Actions": ["github actions"],
        "pytest": ["pytest"],
        "tox": ["tox"],
        "Poetry": ["poetry"],
        "pip": ["pip install"],
        "Conda": ["conda"],
        "Redis": ["redis"],
        "PostgreSQL": ["postgresql", "postgres"],
        "MySQL": ["mysql"],
        "SQLite": ["sqlite"],
    }

    def analyze(
        self,
        repository: RepositoryMetadata,
        readme: str = "",
    ) -> SkillProfile:
        """
        Analyze repository skills.
        """

        language = repository.language or "Unknown"

        required_skills = list(
            self.LANGUAGE_SKILLS.get(
                language,
                [
                    language,
                    "Git",
                ],
            )
        )

        frameworks = self._detect_frameworks(readme)

        recommended_tools = self._detect_tools(readme)

        difficulty = self._difficulty(
            repository,
            frameworks,
        )

        reasons = [
            f"Primary language is {language}.",
            f"Repository has {repository.stars:,} stars.",
        ]

        if frameworks:
            reasons.append("Detected common frameworks from repository documentation.")

        return SkillProfile(
            primary_language=language,
            difficulty=difficulty,
            required_skills=sorted(set(required_skills)),
            recommended_tools=sorted(set(recommended_tools)),
            frameworks=frameworks,
            reasons=reasons,
        )

    # --------------------------------------------------------------
    # Framework Detection
    # --------------------------------------------------------------

    def _detect_frameworks(
        self,
        readme: str,
    ) -> list[str]:

        text = readme.lower()

        frameworks = []

        for framework, keywords in self.FRAMEWORK_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                frameworks.append(framework)

        return frameworks

    # --------------------------------------------------------------
    # Tool Detection
    # --------------------------------------------------------------

    def _detect_tools(
        self,
        readme: str,
    ) -> list[str]:

        text = readme.lower()

        tools = ["Git", "GitHub"]

        for tool, keywords in self.TOOL_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                tools.append(tool)

        return tools

    # --------------------------------------------------------------
    # Difficulty Estimation
    # --------------------------------------------------------------

    def _difficulty(
        self,
        repository: RepositoryMetadata,
        frameworks: list[str],
    ) -> str:

        score = 0

        if repository.stars >= 10000:
            score += 3
        elif repository.stars >= 1000:
            score += 2
        else:
            score += 1

        score += min(len(frameworks), 3)

        if score >= 5:
            return "Advanced"

        if score >= 3:
            return "Intermediate"

        return "Beginner"
