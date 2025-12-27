# =============================================================================
# Test: word_count
# =============================================================================

"""
Tests for rite.text.analysis.word_count.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.analysis.word_count import (
    word_count,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_word_count() -> None:
    """Test word_count() function."""
    # Test basic count
    assert word_count("hello world") == 2
    assert word_count("one two three four five") == 5
    
    # Test empty string
    assert word_count("") == 0
    assert word_count("   ") == 0
    
    # Test single word
    assert word_count("hello") == 1
