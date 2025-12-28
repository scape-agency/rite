# =============================================================================
# Test: cipher_caesar
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_caesar.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.crypto.cipher.cipher_caesar import (
    decode_caesar_cipher,
    encode_caesar_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_caesar_cipher() -> None:
    """Test encode_caesar_cipher() function."""
    result = encode_caesar_cipher("HELLO", 3)
    assert result == "KHOOR"
    assert isinstance(result, str)


def test_decode_caesar_cipher() -> None:
    """Test decode_caesar_cipher() function."""
    result = decode_caesar_cipher("KHOOR", 3)
    assert result == "HELLO"
    assert isinstance(result, str)


def test_encode_caesar_cipher_with_non_alpha() -> None:
    """Test encode_caesar_cipher() preserves non-alphabetic characters."""
    result = encode_caesar_cipher("Hello, World! 123", 3)
    assert result == "Khoor, Zruog! 123"
    # Numbers, spaces, and punctuation should be unchanged
    assert "," in result
    assert " " in result
    assert "123" in result
