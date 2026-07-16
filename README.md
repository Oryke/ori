# 🚀 ORION

> **Open Repository Intelligence & Onboarding Navigator**

ORION is an open-source command-line tool that analyzes GitHub repositories and produces actionable intelligence to help developers understand a project before contributing.

Instead of spending hours exploring unfamiliar repositories, ORION summarizes repository health, governance, documentation quality, contributor readiness, risks, and onboarding recommendations in seconds.

---

## ✨ Features

- 📊 Repository evaluation and scoring
- ❤️ Repository health assessment
- 📚 Documentation analysis
- ⚠️ Repository risk analysis
- 🧑‍💻 Developer fit recommendations
- 🛣️ Personalized contributor roadmap
- 🛡️ Governance evaluation
- 🧠 Skills identification
- 📦 Clean modular CLI
- ✅ Comprehensive automated tests

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Oryke/ori.git
cd ori
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install ORION:

```bash
pip install -e .
```

---

## 🚀 Usage

Analyze a repository:

```bash
python -m ori.cli analyze https://github.com/owner/repository
```

Repository health:

```bash
python -m ori.cli health https://github.com/owner/repository
```

Risk analysis:

```bash
python -m ori.cli risk https://github.com/owner/repository
```

Contributor roadmap:

```bash
python -m ori.cli roadmap https://github.com/owner/repository
```

---

## 📋 Example Output

```text
ORI Analysis
========================================

Repository: Oryke/ori

Overall Score: 72/100

Overall Rating: ★★★☆☆ Fair

Strengths

✓ Repository includes a README
✓ Installation instructions available
✓ Contribution guidelines detected

Advice

- Recommended skill: Python
- Target the main branch
- Read the README before contributing
```

---

## 🏗️ Project Structure

```
src/
├── collector/
├── intelligence/
├── reporter.py
├── commands/
│   ├── analyze.py
│   ├── health.py
│   ├── risk.py
│   └── roadmap.py
└── cli.py
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🛣️ Roadmap

### Current

- Repository analysis
- Health evaluation
- Risk assessment
- Documentation analysis
- Developer fit
- Contributor roadmap
- Governance analysis

### Planned

- Skills command
- Documentation command
- Repository comparison
- AI-powered onboarding assistant
- Repository architecture explanation
- PyPI release

---

## 🤝 Contributing

Contributions are welcome.

Please read the project's **CONTRIBUTING.md** before opening an issue or submitting a pull request.

---

## 🔒 Security

If you discover a security issue, please follow the instructions in **SECURITY.md**.

---

## 📄 License

This project is licensed under the MIT License.

See **LICENSE** for details.

---

## 👩‍💻 Author

**Cynthia Palmata Oke**

GitHub: https://github.com/Oryke

---

## 🌟 Vision

ORION aims to become the intelligent onboarding companion for open-source software.

Rather than simply inspecting repositories, ORION's long-term vision is to help developers answer questions like:

- Is this repository suitable for my experience level?
- Where should I begin contributing?
- Which files should I read first?
- What skills do I need?
- What are the project's health and risks?

By combining repository intelligence with onboarding guidance, ORION helps developers contribute with confidence.