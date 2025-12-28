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
