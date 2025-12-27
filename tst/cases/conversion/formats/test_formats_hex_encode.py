# =============================================================================
# Test: formats_hex_encode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_hex_encode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.formats.formats_hex_encode import (
    formats_hex_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_hex_encode() -> None:
    """Test formats_hex_encode() function."""
    # Test basic encode with bytes
    assert formats_hex_encode(b"hello") == "68656c6c6f"
    assert formats_hex_encode(b"world") == "776f726c64"

    # Test with string
    assert formats_hex_encode("hello") == "68656c6c6f"

    # Test empty
    assert formats_hex_encode(b"") == ""
    assert formats_hex_encode("") == ""
