# =============================================================================
# Test: text_pad_left
# =============================================================================

"""
Tests for rite.text.manipulation.text_pad_left.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.manipulation.text_pad_left import (
    text_pad_left,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_text_pad_left() -> None:
    """Test text_pad_left() function."""
    # Pad with zeros
    assert text_pad_left("5", 3, "0") == "005"

    # Pad with spaces
    assert text_pad_left("Hi", 5) == "   Hi"

    # No padding needed
    assert text_pad_left("Hello", 3) == "Hello"
