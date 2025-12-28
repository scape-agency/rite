# =============================================================================
# Test: cipher_scytale
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_scytale.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_scytale import (
    decode_scytale_cipher,
    encode_scytale_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_scytale_cipher() -> None:
    """Test encode_scytale_cipher() function."""
    result = encode_scytale_cipher("HELLO", 3)
    assert isinstance(result, str)
    assert len(result) >= len("HELLO")


def test_decode_scytale_cipher() -> None:
    """Test decode_scytale_cipher() function."""
    encoded = encode_scytale_cipher("HELLO", 3)
    result = decode_scytale_cipher(encoded, 3)
    assert result == "HELLO"
    assert isinstance(result, str)
