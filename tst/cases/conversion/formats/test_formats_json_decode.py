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

# Import | Libraries
import pytest

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
    assert formats_json_decode("true") == True
    assert formats_json_decode("null") is None
