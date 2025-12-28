# =============================================================================
# Test: markdown_escape
# =============================================================================

"""
Tests for rite.markup.markdown.markdown_escape.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.markup.markdown.markdown_escape import (
    markdown_escape,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_markdown_escape() -> None:
    """Test markdown_escape() function."""
    # Test escaping markdown special characters
    assert markdown_escape("*not italic*") == "\\\\*not italic\\\\*"
    assert markdown_escape("_not italic_") == "\\\\_not italic\\\\_"
    assert markdown_escape("# Not a heading") == "\\\\# Not a heading"

    # Test brackets and parentheses
    assert markdown_escape("[not](link)") == "\\\\[not\\\\]\\\\(link\\\\)"

    # Test backticks
    assert markdown_escape("`not code`") == "\\\\`not code\\\\`"

    # Test tilde
    assert (
        markdown_escape("~not strikethrough~") == "\\\\~not strikethrough\\\\~"
    )

    # Test empty string
    assert markdown_escape("") == ""

    # Test plain text with no special characters
    assert markdown_escape("Plain text") == "Plain text"

    # Test multiple special characters
    assert (
        markdown_escape("*_#[]()`~")
        == "\\\\*\\\\_\\\\#\\\\[\\\\]\\\\(\\\\)\\\\`\\\\~"
    )

    # Test mixed content
    assert (
        markdown_escape("Visit *my site* at [example](http://example.com)")
        == "Visit \\\\*my site\\\\* at \\\\[example\\\\]\\\\(http://example.com\\\\)"
    )
