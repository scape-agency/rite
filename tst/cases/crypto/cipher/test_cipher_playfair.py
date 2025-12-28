# =============================================================================
# Test: cipher_playfair
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_playfair.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_playfair import (
    create_playfair_square,
    decode_playfair_cipher,
    encode_playfair_cipher,
    find_position,
    playfair_cipher_pair,
    prepare_text,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_create_playfair_square() -> None:
    """Test create_playfair_square() function."""
    square = create_playfair_square("KEY")
    assert isinstance(square, list)
    assert len(square) == 5
    assert all(len(row) == 5 for row in square)


def test_find_position() -> None:
    """Test find_position() function."""
    square = create_playfair_square("KEY")
    row, col = find_position("A", square)
    assert isinstance(row, int)
    assert isinstance(col, int)


def test_playfair_cipher_pair() -> None:
    """Test playfair_cipher_pair() function."""
    square = create_playfair_square("KEY")
    pair = playfair_cipher_pair("HE", square, mode="encode")
    assert isinstance(pair, str)
    assert len(pair) == 2


def test_prepare_text() -> None:
    """Test prepare_text() function."""
    result = prepare_text("HELLO")
    assert isinstance(result, str)
    assert len(result) % 2 == 0


def test_encode_playfair_cipher() -> None:
    """Test encode_playfair_cipher() function."""
    result = encode_playfair_cipher("HELLO", "KEY")
    assert isinstance(result, str)
    assert len(result) % 2 == 0


def test_decode_playfair_cipher() -> None:
    """Test decode_playfair_cipher() function."""
    encoded = encode_playfair_cipher("HELLO", "KEY")
    result = decode_playfair_cipher(encoded, "KEY")
    assert isinstance(result, str)
    assert len(result) == len(encoded)
