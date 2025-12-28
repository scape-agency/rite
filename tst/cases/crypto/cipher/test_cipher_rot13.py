# =============================================================================
# Test: cipher_rot13
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_rot13.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_rot13 import (
    decode_rot13_cipher,
    encode_rot13_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_rot13_cipher() -> None:
    """Test encode_rot13_cipher() function."""
    result = encode_rot13_cipher("HELLO")
    assert result == "URYYB"
    assert isinstance(result, str)


def test_decode_rot13_cipher() -> None:
    """Test decode_rot13_cipher() function."""
    result = decode_rot13_cipher("URYYB")
    assert result == "HELLO"
    assert isinstance(result, str)
