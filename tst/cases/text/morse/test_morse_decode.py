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
