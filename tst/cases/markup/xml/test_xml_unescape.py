# =============================================================================
# Test: xml_unescape
# =============================================================================

"""
Tests for rite.markup.xml.xml_unescape.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.markup.xml.xml_unescape import (
    xml_unescape,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_xml_unescape() -> None:
    """Test xml_unescape() function."""
    # Test basic XML entities
    assert xml_unescape("&lt;tag&gt;value&lt;/tag&gt;") == "<tag>value</tag>"
    assert xml_unescape("&lt;root&gt;&lt;/root&gt;") == "<root></root>"

    # Test all basic entities
    assert xml_unescape("&amp;&apos;&quot;") == "&'\""
    assert xml_unescape("&lt;&gt;&amp;") == "<>&"

    # Test no escaping needed
    assert xml_unescape("plain text") == "plain text"
    assert xml_unescape("123456") == "123456"

    # Test empty string
    assert xml_unescape("") == ""

    # Test multiple entities
    assert (
        xml_unescape("&lt;a href=&quot;url&quot;&gt;link&lt;/a&gt;")
        == '<a href="url">link</a>'
    )

    # Test consecutive entities
    assert xml_unescape("&amp;&amp;&amp;") == "&&&"

    # Test single entity
    assert xml_unescape("&lt;") == "<"
    assert xml_unescape("&gt;") == ">"
    assert xml_unescape("&amp;") == "&"
    assert xml_unescape("&apos;") == "'"
    assert xml_unescape("&quot;") == '"'

    # Test mixed content
    assert xml_unescape("Hello &lt;World&gt;!") == "Hello <World>!"
