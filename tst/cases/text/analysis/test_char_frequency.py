# =============================================================================
# Test: char_frequency
# =============================================================================

"""
Tests for rite.text.analysis.char_frequency.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.analysis.char_frequency import (
    char_frequency,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_char_frequency() -> None:
    """Test char_frequency() function."""
    # Test basic frequency
    result = char_frequency("hello")
    assert result == {"h": 1, "e": 1, "l": 2, "o": 1}

    # Test with repeated characters
    result = char_frequency("aabbcc")
    assert result == {"a": 2, "b": 2, "c": 2}

    # Test empty string
    assert char_frequency("") == {}
