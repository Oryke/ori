"""
Tests for the Repository Documentation Analyzer.
"""

from intelligence.documentation import DocumentationAnalyzer


def test_empty_readme_is_detected():
    analyzer = DocumentationAnalyzer()

    documentation = analyzer.analyze("")

    assert documentation.has_readme is False
    assert (
        documentation.summary
        == "Documentation is minimal and may make onboarding difficult."
    )


def test_installation_and_usage_are_detected():
    analyzer = DocumentationAnalyzer()

    readme = """
# ORI

## Installation

pip install ori

## Usage

python -m ori.cli
"""

    documentation = analyzer.analyze(readme)

    assert documentation.has_readme is True
    assert documentation.has_installation is True
    assert documentation.has_usage_examples is True


def test_contributing_license_and_api_are_detected():
    analyzer = DocumentationAnalyzer()

    readme = """
## Contributing

Please read the contribution guide.

## API Reference

REST API

## License

Licensed under the MIT License.
"""

    documentation = analyzer.analyze(readme)

    assert documentation.has_contributing_guide is True
    assert documentation.has_api_documentation is True
    assert documentation.has_license_section is True


def test_beginner_friendly_keywords_are_detected():
    analyzer = DocumentationAnalyzer()

    readme = """
Good First Issue

Beginner contributors are welcome.

Help Wanted
"""

    documentation = analyzer.analyze(readme)

    assert documentation.beginner_friendly is True


def test_excellent_documentation_receives_excellent_summary():
    analyzer = DocumentationAnalyzer()

    readme = """
# ORI

## Installation

pip install ori

## Usage

python -m ori.cli

## Contributing

Contribution guide

## API Reference

REST API

## License

Licensed under MIT

Good first issue
"""

    documentation = analyzer.analyze(readme)

    assert documentation.summary == (
        "Excellent documentation with comprehensive onboarding information."
    )


def test_basic_documentation_receives_basic_summary():
    analyzer = DocumentationAnalyzer()

    readme = """
# ORI

## Installation

pip install ori
"""

    documentation = analyzer.analyze(readme)

    assert (
        documentation.summary
        == "Basic documentation is available but could be improved."
    )


def test_good_documentation_receives_good_summary():
    analyzer = DocumentationAnalyzer()

    readme = """
# ORI

## Installation

pip install ori

## Usage

python -m ori.cli

## Contributing

Contribution guide
"""

    documentation = analyzer.analyze(readme)

    assert (
        documentation.summary
        == "Good documentation covering most contributor needs."
    )