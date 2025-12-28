# =============================================================================
# Test: cipher_four_square
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_four_square.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_four_square import (
    decode_four_square_cipher,
    encode_four_square_cipher,
    find_position,
    four_square_cipher_pair,
    generate_square,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_generate_square() -> None:
    """Test generate_square() function."""
    square = generate_square("KEY")
    assert isinstance(square, list)
    assert len(square) == 5
    assert all(len(row) == 5 for row in square)


def test_find_position() -> None:
    """Test find_position() function."""
    square = generate_square("KEY")
    row, col = find_position("A", square)
    assert isinstance(row, int)
    assert isinstance(col, int)


def test_four_square_cipher_pair() -> None:
    """Test four_square_cipher_pair() function."""
    square_tl = generate_square("")
    square_tr = generate_square("KEY1")
    square_bl = generate_square("KEY2")
    square_br = generate_square("")
    pair = four_square_cipher_pair(
        "HE", square_tl, square_tr, square_bl, square_br, mode="encode"
    )
    assert isinstance(pair, str)
    assert len(pair) == 2


def test_encode_four_square_cipher() -> None:
    """Test encode_four_square_cipher() function."""
    result = encode_four_square_cipher("HELLO", "KEY1", "KEY2")
    assert isinstance(result, str)
    assert len(result) % 2 == 0


def test_decode_four_square_cipher() -> None:
    """Test decode_four_square_cipher() function."""
    encoded = encode_four_square_cipher("HELLO", "KEY1", "KEY2")
    result = decode_four_square_cipher(encoded, "KEY1", "KEY2")
    assert isinstance(result, str)
    assert len(result) == len(encoded)


def test_find_position_not_found() -> None:
    """Test find_position with letter not in square (line 73)."""
    square = generate_square("KEY")
    # J is typically omitted from Playfair-type squares
    with pytest.raises(ValueError, match="not found in square"):
        find_position("J", square)


def test_four_square_cipher_pair_invalid_pair() -> None:
    """Test cipher_pair with invalid pair length (line 99)."""
    square = generate_square("")
    with pytest.raises(ValueError, match="exactly two"):
        four_square_cipher_pair("ABC", square, square, square, square)


def test_four_square_cipher_pair_invalid_mode() -> None:
    """Test cipher_pair with invalid mode (line 112)."""
    square_tl = generate_square("")
    square_tr = generate_square("KEY1")
    square_bl = generate_square("KEY2")
    square_br = generate_square("")
    with pytest.raises(ValueError, match="encode.*decode"):
        four_square_cipher_pair(
            "HE", square_tl, square_tr, square_bl, square_br, mode="invalid"
        )
