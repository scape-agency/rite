# =============================================================================
# Test: morse_encode
# =============================================================================

"""
Tests for rite.text.morse.morse_encode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.morse.morse_encode import (
    morse_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_morse_encode() -> None:
    """Test morse_encode() function."""
    result = morse_encode("hello")
    assert isinstance(result, str)
    assert len(result) > 0


def test_morse_encode_hello() -> None:
    """Test morse_encode with known output."""
    result = morse_encode("HELLO")
    assert result == ".... . .-.. .-.. ---"


def test_morse_encode_with_numbers() -> None:
    """Test morse_encode with numbers."""
    result = morse_encode("SOS 123")
    assert "..." in result  # S
    assert "---" in result  # O
    assert "/" in result  # space


def test_morse_encode_custom_separator() -> None:
    """Test morse_encode with custom separator."""
    result = morse_encode("HI", separator="|")
    assert "|" in result


def test_morse_encode_unknown_chars() -> None:
    """Test morse_encode skips unknown characters (line 83->82)."""
    # @ and # are not in MORSE_CODE_DICT, should be skipped
    result = morse_encode("A@B#C")
    # Should encode A, B, C only
    assert result == ".- -... -.-."
