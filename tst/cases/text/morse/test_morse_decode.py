# =============================================================================
# Test: morse_decode
# =============================================================================

"""
Tests for rite.text.morse.morse_decode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.morse.morse_decode import (
    morse_decode,
)
from rite.text.morse.morse_encode import (
    morse_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_morse_decode() -> None:
    """Test morse_decode() function."""
    morse_code = morse_encode("a")
    result = morse_decode(morse_code)
    assert isinstance(result, str)


def test_morse_decode_hello() -> None:
    """Test morse_decode for HELLO."""
    result = morse_decode(".... . .-.. .-.. ---")
    assert result == "HELLO"


def test_morse_decode_with_numbers() -> None:
    """Test morse_decode with numbers."""
    result = morse_decode(".---- ..--- ...--")
    assert result == "123"


def test_morse_decode_with_space() -> None:
    """Test morse_decode with space separator."""
    result = morse_decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
    assert result == "HELLO WORLD"


def test_morse_decode_invalid_sequence() -> None:
    """Test morse_decode with invalid Morse code sequence."""
    with pytest.raises(ValueError, match="Invalid Morse code sequence"):
        morse_decode(".... . .-.. .-.. .-.-.-.-.-.")


def test_morse_decode_empty_string() -> None:
    """Test morse_decode with empty string."""
    result = morse_decode("")
    assert result == ""


def test_morse_decode_custom_separator() -> None:
    """Test morse_decode with custom separator."""
    result = morse_decode("....|.|.-..|.-..|---", separator="|")
    assert result == "HELLO"


def test_morse_decode_roundtrip() -> None:
    """Test encode/decode roundtrip."""
    original = "HELLO WORLD"
    encoded = morse_encode(original)
    decoded = morse_decode(encoded)
    assert decoded == original
