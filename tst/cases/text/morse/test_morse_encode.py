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
