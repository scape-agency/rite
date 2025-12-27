# =============================================================================
# Test: shortest_word
# =============================================================================

"""
Tests for rite.text.analysis.shortest_word.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.analysis.shortest_word import (
    shortest_word,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_shortest_word() -> None:
    """Test shortest_word() function."""
    # Test basic shortest (both same length, returns first)
    assert shortest_word("hello world") == "hello"
    assert shortest_word("abc defgh") == "abc"
    
    # Test different lengths
    assert shortest_word("a bb ccc") == "a"
    
    # Test single word
    assert shortest_word("hello") == "hello"
    
    # Test error on empty string
    with pytest.raises(ValueError, match="Text contains no words"):
        shortest_word("")
    
    with pytest.raises(ValueError, match="Text contains no words"):
        shortest_word("   ")
