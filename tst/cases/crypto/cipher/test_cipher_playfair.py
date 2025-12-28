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


def test_find_position_not_found() -> None:
    """Test find_position with letter not in square (line 74)."""
    square = create_playfair_square("KEY")
    # J is replaced with I in Playfair
    with pytest.raises(ValueError, match="not found in square"):
        find_position("J", square)


def test_playfair_cipher_pair_same_row() -> None:
    """Test cipher_pair with same row (lines 104-105)."""
    square = create_playfair_square("KEY")
    # Create a pair that will be in the same row
    # "KE" should be in same row since they're at start of key
    pair = playfair_cipher_pair("AB", square, mode="encode")
    decoded = playfair_cipher_pair(pair, square, mode="decode")
    assert decoded == "AB"


def test_playfair_cipher_pair_same_column() -> None:
    """Test cipher_pair with same column (lines 104-105)."""
    square = create_playfair_square("")  # Standard square
    # Find letters in the same column - A and F should be in same column
    # Standard square: ABCDE/FGHIK/LMNOP/QRSTU/VWXYZ
    pair_encoded = playfair_cipher_pair("AF", square, mode="encode")
    pair_decoded = playfair_cipher_pair(pair_encoded, square, mode="decode")
    assert pair_decoded == "AF"


def test_prepare_text_with_j() -> None:
    """Test prepare_text replaces J with I (line 136)."""
    result = prepare_text("JELLO")
    assert "J" not in result
    assert "I" in result or result.startswith("I")


def test_prepare_text_single_char_end() -> None:
    """Test prepare_text pads single char at end (line 136)."""
    result = prepare_text("ABC")
    # AB + CX (padded)
    assert len(result) % 2 == 0
