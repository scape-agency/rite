# =============================================================================
# Test: cipher_autokey
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_autokey.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_autokey import (
    decode_autokey_cipher,
    encode_autokey_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_autokey_cipher() -> None:
    """Test encode_autokey_cipher() function."""
    result = encode_autokey_cipher("HELLO", "KEY")
    assert isinstance(result, str)
    assert len(result) == len("HELLO")


def test_decode_autokey_cipher() -> None:
    """Test decode_autokey_cipher() function."""
    encoded = encode_autokey_cipher("HELLO", "KEY")
    result = decode_autokey_cipher(encoded, "KEY")
    assert result == "HELLO"
    assert isinstance(result, str)


def test_encode_autokey_cipher_with_non_alpha() -> None:
    """Test encoding with non-alpha characters (line 84)."""
    # Test with punctuation - should preserve non-alpha chars
    result = encode_autokey_cipher("HI!", "KEY")
    assert "!" in result
    assert len(result) == 3


def test_decode_autokey_cipher_with_non_alpha() -> None:
    """Test decoding with non-alpha characters (line 117)."""
    # Directly test the decode function with non-alpha
    decoded = decode_autokey_cipher("K1Y", "KEY")
    assert "1" in decoded  # Non-alpha preserved


def test_autokey_cipher_lowercase() -> None:
    """Test with lowercase letters."""
    result = encode_autokey_cipher("hello", "key")
    assert isinstance(result, str)
    decoded = decode_autokey_cipher(result, "key")
    assert decoded == "hello"
