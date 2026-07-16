# ORI

<p align="center">
  <img src="./assets/preview.png" alt="ORI Preview" width="900">
</p>

> **The intelligence layer for open source.**

ORI (**Open Repository Intelligence**) is an open-source project that analyzes public GitHub repositories and transforms repository data into actionable intelligence for developers, contributors, maintainers, and open-source communities.

Rather than manually inspecting repository activity, documentation, governance, and contribution readiness, ORI provides a structured assessment that helps developers quickly understand a project's quality, maturity, and contribution potential.

---

# Why ORI Exists

Modern software development has excellent tools for writing, testing, and deploying code.

Open-source communities, however, still face challenges that traditional development tools do not solve.

- Maintainers experience burnout.
- New contributors struggle to find where to begin.
- Documentation becomes outdated.
- Healthy repositories are difficult to distinguish from abandoned ones.
- Developers spend significant time evaluating projects before contributing.

ORI exists to make repository evaluation easier by turning repository data into meaningful intelligence that supports better contribution decisions.

---

# Features

The current version of ORI includes:

- Repository metadata collection
- Repository health analysis
- Documentation quality assessment
- Repository risk evaluation
- Contributor skill profiling
- Developer fit analysis
- Personalized contribution roadmap generation
- Overall repository evaluation and scoring
- Repository insights and recommendations
- Open issue discovery
- Human-readable terminal reports

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Oryke/Ori.git
cd ori
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run ORI from the command line:

```bash
python -m ori.cli
```

When prompted, enter a public GitHub repository URL:

```text
https://github.com/psf/requests
```

ORI will generate an intelligence report containing:

- Repository Summary
- Repository Statistics
- Repository Health
- Documentation Analysis
- Repository Risk
- Developer Skills
- Developer Fit
- Contribution Roadmap
- Repository Evaluation
- Insights
- Recommendations
- Open Issues

---

# Example Output

```text
Repository: psf/requests

Overall Score: 89/100
Overall Rating: ★★★★☆ Good

Strengths
✓ Repository demonstrates strong overall health.
✓ Installation instructions are available.
✓ Usage examples are provided.

Weaknesses
• Repository has no contribution guide.

Recommended For
✓ Production use
✓ Learning
✓ Open-source contribution
```

---

# Project Architecture

```
                GitHub Repository
                        │
                        ▼
              Repository Collectors
                        │
                        ▼
             Repository Intelligence
        ┌────────────────────────────┐
        │ Repository Analyzer        │
        │ Health Engine              │
        │ Documentation Analyzer     │
        │ Risk Analyzer              │
        │ Skill Analyzer             │
        │ Developer Fit Analyzer     │
        │ Roadmap Generator          │
        └────────────────────────────┘
                        │
                        ▼
             Repository Evaluator
                        │
                        ▼
              Repository Reporter
                        │
                        ▼
                 CLI Intelligence Report
```

---

# Project Structure

```
ORI/
│
├── src/
│   ├── collector/
│   ├── intelligence/
│   └── ori/
│
├── tests/
│
├── assets/
│
├── README.md
├── pyproject.toml
├── requirements.txt
└── LICENSE
```

---

# Running Tests

Run the complete test suite:

```bash
pytest
```

Format the project:

```bash
ruff format .
```

Run static analysis:

```bash
ruff check .
```

---

# Current Status

ORI is currently an actively developed prototype.

The project already provides a complete command-line workflow for collecting repository information, generating repository intelligence, evaluating contribution readiness, and producing structured reports.

Future releases will continue expanding ORI's intelligence capabilities and reporting features.

---

# Roadmap

Planned improvements include:

- Markdown report export
- JSON report export
- HTML report generation
- Repository comparison
- Historical repository tracking
- GitHub Actions integration
- GitLab repository support
- Additional intelligence engines
- Expanded automated test coverage

---

# Contributing

Contributions are welcome.

Whether you're interested in repository analysis, intelligence engines, testing, documentation, or improving the developer experience, we'd love your contributions.

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Add or update tests where appropriate.
5. Submit a pull request.

---

# License

This project is licensed under the MIT License.