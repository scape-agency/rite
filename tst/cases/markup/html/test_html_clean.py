# =============================================================================
# Test: html_clean
# =============================================================================

"""
Tests for rite.markup.html.html_clean.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.markup.html.html_clean import (
    html_clean,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_html_clean() -> None:
    """Test html_clean() function."""
    # Test basic tag removal
    assert html_clean("<p>Hello</p>") == "Hello"
    assert html_clean("<p>Hello <b>World</b></p>") == "Hello World"

    # Test with various HTML tags
    assert html_clean("<div>Content</div>") == "Content"
    assert html_clean("<span>Text</span>") == "Text"
    assert html_clean("<a href='#'>Link</a>") == "Link"

    # Test with nested tags
    assert html_clean("<div><p><span>Nested</span></p></div>") == "Nested"

    # Test with strip=False preserves whitespace
    result = html_clean("<div>  Text  </div>", strip=False)
    assert result == "  Text  "

    # Test empty tags
    assert html_clean("<p></p>") == ""
    assert html_clean("<div><br/></div>") == ""

    # Test with attributes
    assert html_clean('<div class="test" id="main">Content</div>') == "Content"

    # Test no tags present
    assert html_clean("Plain text") == "Plain text"
