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

    # Test with spaces
    assert formats_hex_decode("68 65 6c 6c 6f") == b"hello"
    assert formats_hex_decode("77 6f 72 6c 64") == b"world"

    # Test with default on invalid input
    assert formats_hex_decode("invalid!@#$%") is None
    assert formats_hex_decode("invalid!@#$%", b"") == b""
    assert formats_hex_decode("ZZ ZZ ZZ", b"fallback") == b"fallback"

    # Test hex with special bytes
    assert formats_hex_decode("00010203") == b"\x00\x01\x02\x03"

    # Test mixed case
    assert formats_hex_decode("48454c4c4f") == b"HELLO"

    # Test with spaces
    assert formats_hex_decode("68 65 6c 6c 6f") == b"hello"
    assert formats_hex_decode("48 45 4C 4C 4F") == b"HELLO"

    # Test with default on invalid input
    assert formats_hex_decode("invalid") is None
    assert formats_hex_decode("ZZZ", b"") == b""
    assert formats_hex_decode("not-hex", b"fallback") == b"fallback"

    # Test special bytes
    assert formats_hex_decode("0102030405") == b"\x01\x02\x03\x04\x05"
    assert formats_hex_decode("ff fe fd") == b"\xff\xfe\xfd"
