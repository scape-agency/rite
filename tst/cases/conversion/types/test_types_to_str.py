# =============================================================================
# Test: types_to_str
# =============================================================================

"""
Tests for rite.conversion.types.types_to_str.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_str import (
    types_to_str,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_types_to_str_basic_behaviour() -> None:
    """Test conversion of common values to string."""
    assert types_to_str(42) == "42"
    assert types_to_str("text") == "text"

    raw = "hello"
    assert types_to_str(raw) is raw

    assert types_to_str(None) == ""
    assert types_to_str(None, none_as_empty=False) == "None"


def test_types_to_str_bytes_decoding() -> None:
    """Test that bytes are decoded using the given encoding."""
    value = "héllo".encode("utf-8")
    assert types_to_str(value) == "héllo"
