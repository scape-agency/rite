# =============================================================================
# Test: cipher_xor
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_xor.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_xor import (
    decode_xor_cipher,
    encode_xor_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_xor_cipher() -> None:
    """Test encode_xor_cipher() function."""
    result = encode_xor_cipher("HELLO", "KEY")
    assert isinstance(result, str)
    assert result != "HELLO"


def test_decode_xor_cipher() -> None:
    """Test decode_xor_cipher() function."""
    encoded = encode_xor_cipher("HELLO", "KEY")
    result = decode_xor_cipher(encoded, "KEY")
    assert result == "HELLO"
    assert isinstance(result, str)
