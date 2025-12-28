# =============================================================================
# Test: html_escape
# =============================================================================

"""
Tests for rite.markup.html.html_escape.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.html.html_escape import (
    html_escape,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_html_escape() -> None:
    """Test html_escape() function."""
    # Test basic escaping
    assert html_escape("<div>") == "&lt;div&gt;"
    assert html_escape("&") == "&amp;"

    # Test complex HTML
    assert (
        html_escape("<div>Hello & goodbye</div>")
        == "&lt;div&gt;Hello &amp; goodbye&lt;/div&gt;"
    )

    # Test comparison operators
    assert html_escape("5 < 10 & 10 > 5") == "5 &lt; 10 &amp; 10 &gt; 5"

    # Test quotes
    assert html_escape('"quoted"') == "&quot;quoted&quot;"
    assert html_escape("'single'") == "&#x27;single&#x27;"

    # Test empty string
    assert html_escape("") == ""

    # Test plain text (no special characters)
    assert html_escape("Hello World") == "Hello World"

    # Test multiple special characters
    assert (
        html_escape("<script>alert('xss')</script>")
        == "&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;"
    )
