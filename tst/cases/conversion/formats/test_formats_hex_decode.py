# =============================================================================
# Test: formats_hex_decode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_hex_decode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.formats.formats_hex_decode import (
    formats_hex_decode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_hex_decode() -> None:
    """Test formats_hex_decode() function."""
    # Test basic decode
    assert formats_hex_decode("68656c6c6f") == b"hello"
    assert formats_hex_decode("776f726c64") == b"world"

    # Test uppercase
    assert formats_hex_decode("48454C4C4F") == b"HELLO"

    # Test empty
    assert formats_hex_decode("") == b""
