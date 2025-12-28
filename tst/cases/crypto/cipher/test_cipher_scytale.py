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


def test_encode_scytale_invalid_diameter() -> None:
    """Test encoding with invalid diameter (line 47)."""
    with pytest.raises(ValueError, match="Diameter must be a positive"):
        encode_scytale_cipher("HELLO", 0)


def test_decode_scytale_invalid_diameter() -> None:
    """Test decoding with invalid diameter (line 80)."""
    with pytest.raises(ValueError, match="Diameter must be a positive"):
        decode_scytale_cipher("HELLO", 0)


def test_encode_scytale_with_padding() -> None:
    """Test encoding with text that needs padding (line 51->54)."""
    # Text length 5 with diameter 3 requires padding
    result = encode_scytale_cipher("HELLO", 3)
    # Should pad to 6 characters (2 rows x 3 cols)
    assert len(result) == 6
