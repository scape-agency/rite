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

# Import | Libraries
import pytest

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
