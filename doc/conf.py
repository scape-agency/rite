# =============================================================================
# Sphinx Configuration
# =============================================================================

"""
Sphinx configuration for Rite documentation.

This configuration integrates with MkDocs via mkdocstrings.
"""

# Import | Standard Library
import os
import sys

# =============================================================================
# Path Setup
# =============================================================================

# Add source directory to Python path
sys.path.insert(0, os.path.abspath("../src"))

# =============================================================================
# Project Information
# =============================================================================

project = "rite"
copyright = "2023-2025, Scape Agency BV"  # pylint: disable=redefined-builtin
author = "Scape Agency"
release = "0.1.2"
version = "0.1.2"

# =============================================================================
# General Configuration
# =============================================================================

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.githubpages",
]

# Templates path
templates_path = ["_templates"]

# Source suffix
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Master document
master_doc = "index"

# Language
language = "en"

# Exclude patterns
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".venv",
    "venv",
    "**/.pytest_cache",
    "**/__pycache__",
]

# Pygments style
pygments_style = "sphinx"

# =============================================================================
# Napoleon Settings (Google/NumPy Style Docstrings)
# =============================================================================

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# =============================================================================
# Autodoc Settings
# =============================================================================

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
    "show-inheritance": True,
}

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
autodoc_type_aliases = {}

# =============================================================================
# Autosummary Settings
# =============================================================================

autosummary_generate = True
autosummary_imported_members = False

# =============================================================================
# Intersphinx Settings
# =============================================================================

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# =============================================================================
# HTML Output Settings
# =============================================================================

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

html_logo = "assets/image/rite_logo_light.png"
html_favicon = "assets/favicon/favicon.ico"

html_context = {
    "display_github": True,
    "github_user": "scape-agency",
    "github_repo": "rite",
    "github_version": "main",
    "conf_py_path": "/doc/",
}

# =============================================================================
# LaTeX Output Settings
# =============================================================================

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
}

latex_documents = [
    (
        master_doc,
        "rite.tex",
        "Rite Documentation",
        "Scape Agency",
        "manual",
    ),
]

# =============================================================================
# Man Page Output Settings
# =============================================================================

man_pages = [(master_doc, "rite", "Rite Documentation", [author], 1)]

# =============================================================================
# Texinfo Output Settings
# =============================================================================

texinfo_documents = [
    (
        master_doc,
        "rite",
        "Rite Documentation",
        author,
        "rite",
        "Python Utility Package",
        "Miscellaneous",
    ),
]

# =============================================================================
# Todo Settings
# =============================================================================

todo_include_todos = True
