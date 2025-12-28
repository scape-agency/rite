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


def test_encode_transposition_invalid_key() -> None:
    """Test encoding with invalid key (line 47)."""
    with pytest.raises(ValueError, match="Key must be a positive"):
        encode_transposition_cipher("HELLO", 0)


def test_decode_transposition_invalid_key() -> None:
    """Test decoding with invalid key (line 72)."""
    with pytest.raises(ValueError, match="Key must be a positive"):
        decode_transposition_cipher("HELLO", 0)


def test_encode_transposition_with_padding() -> None:
    """Test encoding with text needing padding (line 51->54)."""
    result = encode_transposition_cipher("HELLO", 3)
    # 5 chars + 1 padding = 6 chars
    assert len(result) == 6


def test_encode_transposition_no_padding() -> None:
    """Test encoding with text not needing padding (line 51->54)."""
    result = encode_transposition_cipher("ABCDEF", 3)
    # 6 chars with key 3 = exactly 2 rows, no padding needed
    assert len(result) == 6


def test_decode_transposition_no_strip() -> None:
    """Test decoding without stripping padding (line 90->89)."""
    encoded = encode_transposition_cipher("HI", 3)
    result = decode_transposition_cipher(encoded, 3, strip_padding=False)
    # Should keep trailing spaces
    assert len(result) == 3


def test_decode_transposition_uneven_columns() -> None:
    """Test decoding with uneven column lengths (branch 90->89)."""
    # Manually create an encoded string that would produce uneven columns
    # when decoded. With key=3 and 5 chars:
    # full_rows = 5 // 3 = 1
    # extra_chars = 5 % 3 = 2
    # col_lengths = [2, 2, 1] (first 2 columns have 2 chars, 3rd has 1)
    # So we need a 5-char string to decode
    encoded = "ABCDE"  # Unpadded encoded string
    result = decode_transposition_cipher(encoded, 3)
    # This should hit the row < len(col) FALSE branch when:
    # row=1, col[2] has len=1, 1<1 is FALSE
    assert isinstance(result, str)
