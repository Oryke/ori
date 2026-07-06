"""
Shared constants used by ORI's intelligence modules.
"""

# ---------------------------------------------------------------------
# Documentation Detection Keywords
# ---------------------------------------------------------------------

INSTALLATION_KEYWORDS = (
    "installation",
    "install",
    "pip install",
    "poetry install",
    "conda install",
    "npm install",
    "cargo install",
)

USAGE_KEYWORDS = (
    "usage",
    "examples",
    "example",
    "quickstart",
    "quick start",
    "getting started",
    "basic usage",
    "basic example",
    "how to use",
    "import requests",
    ">>>",
)

CONTRIBUTING_KEYWORDS = (
    "contributing",
    "contributing.md",
    "contribution guide",
    "how to contribute",
    "pull request",
)

API_DOCUMENTATION_KEYWORDS = (
    "api",
    "reference",
    "api reference",
    "api documentation",
    "rest api",
)

LICENSE_SECTION_KEYWORDS = (
    "license",
    "licensing",
    "copyright",
)