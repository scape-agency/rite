# =============================================================================
# Test: xml_escape
# =============================================================================

"""
Tests for rite.markup.xml.xml_escape.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.markup.xml.xml_escape import (
    xml_escape,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_xml_escape() -> None:
    """Test xml_escape() function."""
    # Test basic escaping
    assert xml_escape("<tag>") == "&lt;tag&gt;"
    assert xml_escape("&") == "&amp;"

    # Test complex XML
    assert (
        xml_escape("<tag>value & more</tag>")
        == "&lt;tag&gt;value &amp; more&lt;/tag&gt;"
    )

    # Test comparison operators
    assert xml_escape("5 < 10 & 10 > 5") == "5 &lt; 10 &amp; 10 &gt; 5"

    # Test quotes
    assert xml_escape('"quoted"') == "&quot;quoted&quot;"
    assert xml_escape("'quoted'") == "&apos;quoted&apos;"

    # Test empty string
    assert xml_escape("") == ""

    # Test plain text
    assert xml_escape("Hello World") == "Hello World"

    # Test mixed special characters
    assert (
        xml_escape('<root attr="val">text & more</root>')
        == "&lt;root attr=&quot;val&quot;&gt;text &amp; more&lt;/root&gt;"
    )
