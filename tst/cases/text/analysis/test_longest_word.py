# =============================================================================
# Test: longest_word
# =============================================================================

"""
Tests for rite.text.analysis.longest_word.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.analysis.longest_word import (
    longest_word,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_longest_word() -> None:
    """Test longest_word() function."""
    # Test basic longest
    assert longest_word("hello world") == "hello"
    assert longest_word("a bb ccc") == "ccc"
    
    # Test single word
    assert longest_word("hello") == "hello"
    
    # Test error on empty string
    with pytest.raises(ValueError, match="Text contains no words"):
        longest_word("")
    
    with pytest.raises(ValueError, match="Text contains no words"):
        longest_word("   ")
