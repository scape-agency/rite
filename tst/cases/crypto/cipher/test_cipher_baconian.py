# =============================================================================
# Test: cipher_baconian
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_baconian.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_baconian import (
    decode_baconian_cipher,
    encode_baconian_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_baconian_cipher() -> None:
    """Test encode_baconian_cipher() function."""
    result = encode_baconian_cipher("ab")
    assert result == "aaaaaaaaab"
    assert isinstance(result, str)


def test_decode_baconian_cipher() -> None:
    """Test decode_baconian_cipher() function."""
    encoded = encode_baconian_cipher("abc")
    result = decode_baconian_cipher(encoded)
    assert result == "abc"
    assert isinstance(result, str)
