# =============================================================================
# Test: average_word_length
# =============================================================================

"""
Tests for rite.text.analysis.average_word_length.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.analysis.average_word_length import (
    average_word_length,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_average_word_length() -> None:
    """Test average_word_length() function."""
    # Test basic average
    assert average_word_length("hello world") == 5.0
    assert average_word_length("a bb ccc") == 2.0
    
    # Test single word
    assert average_word_length("hello") == 5.0
    
    # Test error on empty string
    with pytest.raises(ValueError, match="Text contains no words"):
        average_word_length("")
    
    with pytest.raises(ValueError, match="Text contains no words"):
        average_word_length("   ")
