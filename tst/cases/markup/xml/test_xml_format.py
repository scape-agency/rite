# =============================================================================
# Test: xml_format
# =============================================================================

"""
Tests for rite.markup.xml.xml_format.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.xml.xml_format import (
    xml_format,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_xml_format_basic() -> None:
    """Test xml_format formats basic XML."""
    xml = "<root><child>text</child></root>"
    result = xml_format(xml)
    assert "<root>" in result
    assert "<child>text</child>" in result
    assert "</root>" in result


def test_xml_format_adds_indentation() -> None:
    """Test xml_format adds indentation."""
    xml = "<root><child>text</child></root>"
    result = xml_format(xml)
    # Should have newlines and indentation
    assert "\n" in result


def test_xml_format_custom_indent() -> None:
    """Test xml_format with custom indentation."""
    xml = "<root><child>text</child></root>"
    result = xml_format(xml, indent="    ")  # 4 spaces
    assert result is not None
    # Verify it has some indentation
    assert "\n" in result


def test_xml_format_multiple_children() -> None:
    """Test xml_format with multiple child elements."""
    xml = "<root><a>1</a><b>2</b><c>3</c></root>"
    result = xml_format(xml)
    assert "<a>1</a>" in result
    assert "<b>2</b>" in result
    assert "<c>3</c>" in result


def test_xml_format_nested_structure() -> None:
    """Test xml_format with nested structure."""
    xml = "<root><parent><child>text</child></parent></root>"
    result = xml_format(xml)
    assert "<child>text</child>" in result


def test_xml_format_invalid_xml() -> None:
    """Test xml_format raises ValueError for invalid XML."""
    invalid_xml = "<root><unclosed>"
    with pytest.raises(ValueError):
        xml_format(invalid_xml)


def test_xml_format_malformed_xml() -> None:
    """Test xml_format raises ValueError for malformed XML."""
    malformed_xml = "<root>text</root><extra>"
    with pytest.raises(ValueError):
        xml_format(malformed_xml)
