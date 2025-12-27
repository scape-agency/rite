# =============================================================================
# Test: formats_json_encode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_json_encode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.formats.formats_json_encode import (
    formats_json_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_json_encode() -> None:
    """Test formats_json_encode() function."""
    # Test basic encode
    assert formats_json_encode({"key": "value"}) == '{"key": "value"}'
    assert formats_json_encode([1, 2, 3]) == "[1, 2, 3]"
    assert formats_json_encode("hello") == '"hello"'
    assert formats_json_encode(123) == "123"
    assert formats_json_encode(True) == "true"
    assert formats_json_encode(None) == "null"
