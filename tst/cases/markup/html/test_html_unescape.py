# =============================================================================
# Test: html_unescape
# =============================================================================

"""
Tests for rite.markup.html.html_unescape.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.html.html_escape import html_escape
from rite.markup.html.html_unescape import (
    html_unescape,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_html_unescape() -> None:
    """Test html_unescape() function."""
    # Test basic unescaping
    assert html_unescape("&lt;div&gt;") == "<div>"
    assert html_unescape("&amp;") == "&"

    # Test complex HTML
    assert html_unescape("&lt;div&gt;Hello&lt;/div&gt;") == "<div>Hello</div>"

    # Test comparison operators
    assert html_unescape("5 &lt; 10 &amp; 10 &gt; 5") == "5 < 10 & 10 > 5"

    # Test quotes
    assert html_unescape("&quot;quoted&quot;") == '"quoted"'

    # Test empty string
    assert html_unescape("") == ""

    # Test plain text (no entities)
    assert html_unescape("Hello World") == "Hello World"

    # Test mixed entities
    assert html_unescape("&lt;p&gt;Hello&lt;/p&gt;") == "<p>Hello</p>"

    # Test round-trip (escape then unescape)
    original = "<div>Hello & goodbye</div>"
    escaped = html_escape(original)
    unescaped = html_unescape(escaped)
    assert unescaped == original
