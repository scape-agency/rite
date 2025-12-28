# =============================================================================
# Test: markdown_to_html
# =============================================================================

"""
Tests for rite.markup.markdown.markdown_to_html.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.markdown.markdown_to_html import (
    markdown_to_html,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_markdown_to_html_headers() -> None:
    """Test markdown_to_html converts headers."""
    assert "<h1>Heading</h1>" in markdown_to_html("# Heading")
    assert "<h2>Sub</h2>" in markdown_to_html("## Sub")
    assert "<h3>Minor</h3>" in markdown_to_html("### Minor")


def test_markdown_to_html_bold() -> None:
    """Test markdown_to_html converts bold text."""
    result = markdown_to_html("**bold**")
    assert "<strong>bold</strong>" in result
    result = markdown_to_html("__bold__")
    assert "<strong>bold</strong>" in result


def test_markdown_to_html_italic() -> None:
    """Test markdown_to_html converts italic text."""
    result = markdown_to_html("*italic*")
    assert "<em>italic</em>" in result
    result = markdown_to_html("_italic_")
    assert "<em>italic</em>" in result


def test_markdown_to_html_code() -> None:
    """Test markdown_to_html converts code."""
    result = markdown_to_html("`code`")
    assert "<code>code</code>" in result


def test_markdown_to_html_mixed() -> None:
    """Test markdown_to_html with mixed formatting."""
    result = markdown_to_html("**bold** and *italic* and `code`")
    assert "<strong>bold</strong>" in result
    assert "<em>italic</em>" in result
    assert "<code>code</code>" in result
