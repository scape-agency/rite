# =============================================================================
# Test: text_wrap
# =============================================================================

"""
Tests for rite.text.manipulation.text_wrap.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.manipulation.text_wrap import (
    text_wrap,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_text_wrap() -> None:
    """Test text_wrap() function."""
    # Wrap short text
    result = text_wrap("Hello World", 5)
    assert result == ["Hello", "World"]
    
    # Wrap longer text
    result = text_wrap("A long sentence", 10)
    assert result == ["A long", "sentence"]
    
    # No wrap needed
    result = text_wrap("Hi", 10)
    assert result == ["Hi"]
