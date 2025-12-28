# =============================================================================
# Test: cipher_vigenere
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_vigenere.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.crypto.cipher.cipher_vigenere import (
    decode_vigenere_cipher,
    encode_vigenere_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_vigenere_cipher() -> None:
    """Test encode_vigenere_cipher() function."""
    result = encode_vigenere_cipher("HELLO", "KEY")
    assert isinstance(result, str)
    assert len(result) == len("HELLO")


def test_decode_vigenere_cipher() -> None:
    """Test decode_vigenere_cipher() function."""
    encoded = encode_vigenere_cipher("HELLO", "KEY")
    result = decode_vigenere_cipher(encoded, "KEY")
    assert result == "HELLO"
    assert isinstance(result, str)


def test_encode_vigenere_cipher_with_non_alpha() -> None:
    """Test encoding with non-alpha characters (line 60)."""
    result = encode_vigenere_cipher("HEL LO!", "KEY")
    assert " " in result
    assert "!" in result


def test_decode_vigenere_cipher_with_non_alpha() -> None:
    """Test decoding with non-alpha characters (line 91)."""
    encoded = encode_vigenere_cipher("A B C", "KEY")
    decoded = decode_vigenere_cipher(encoded, "KEY")
    assert decoded == "A B C"


def test_vigenere_cipher_lowercase() -> None:
    """Test with lowercase letters."""
    encoded = encode_vigenere_cipher("hello", "key")
    decoded = decode_vigenere_cipher(encoded, "key")
    assert decoded == "hello"
