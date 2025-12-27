# =============================================================================
# Test: text_pad_right
# =============================================================================

"""
Tests for rite.text.manipulation.text_pad_right.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.manipulation.text_pad_right import (
    text_pad_right,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_text_pad_right() -> None:
    """Test text_pad_right() function."""
    # Pad with spaces
    assert text_pad_right("Hi", 5) == "Hi   "

    # Pad with zeros
    assert text_pad_right("5", 3, "0") == "500"

    # No padding needed
    assert text_pad_right("Hello", 3) == "Hello"
