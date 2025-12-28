# =============================================================================
# Test: cipher_transposition
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_transposition.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_transposition import (
    decode_transposition_cipher,
    encode_transposition_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_transposition_cipher() -> None:
    """Test encode_transposition_cipher() function."""
    result = encode_transposition_cipher("HELLO", 3)
    assert isinstance(result, str)
    assert len(result) >= len("HELLO")


def test_decode_transposition_cipher() -> None:
    """Test decode_transposition_cipher() function."""
    encoded = encode_transposition_cipher("HELLO", 3)
    result = decode_transposition_cipher(encoded, 3)
    assert result.strip() == "HELLO"
    assert isinstance(result, str)
