# =============================================================================
# Test: text_is_numeric
# =============================================================================

"""
Tests for rite.text.validation.text_is_numeric.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.validation.text_is_numeric import (
    text_is_numeric,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,expected",
    [
        ("123", True),  # All digits
        ("0", True),  # Zero
        ("123abc", False),  # Contains letters
        ("12.34", False),  # Contains decimal
        ("", False),  # Empty
        (" 123", False),  # Contains space
    ],
)
def test_text_is_numeric(text: str, expected: bool) -> None:
    """Test text_is_numeric() with various strings."""
    assert text_is_numeric(text) == expected
