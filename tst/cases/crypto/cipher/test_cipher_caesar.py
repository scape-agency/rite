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

# Import | Libraries
import pytest

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
