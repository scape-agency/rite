# =============================================================================
# Test: formats_json_decode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_json_decode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.conversion.formats.formats_json_decode import (
    formats_json_decode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_json_decode() -> None:
    """Test formats_json_decode() function."""
    # Test basic decode
    assert formats_json_decode('{"key": "value"}') == {"key": "value"}
    assert formats_json_decode("[1, 2, 3]") == [1, 2, 3]
    assert formats_json_decode('"hello"') == "hello"
    assert formats_json_decode("123") == 123
    assert formats_json_decode("true") is True
    assert formats_json_decode("null") is None

    # Test with bytes input
    assert formats_json_decode(b'{"a": 1}') == {"a": 1}
    assert formats_json_decode(b"[1, 2, 3]") == [1, 2, 3]

    # Test with default values on invalid JSON
    assert formats_json_decode("invalid") is None
    assert formats_json_decode("invalid", {}) == {}
    assert formats_json_decode("invalid", []) == []
    assert formats_json_decode("{invalid json}", "default") == "default"

    # Test nested structures
    assert formats_json_decode('{"a": {"b": {"c": 1}}}') == {
        "a": {"b": {"c": 1}}
    }

    # Test with special characters
    assert formats_json_decode('{"emoji": "😀"}') == {"emoji": "😀"}
