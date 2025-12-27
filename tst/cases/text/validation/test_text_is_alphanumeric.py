# =============================================================================
# Test: text_is_alphanumeric
# =============================================================================

"""
Tests for rite.text.validation.text_is_alphanumeric.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.validation.text_is_alphanumeric import (
    text_is_alphanumeric,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,expected",
    [
        ("abc123", True),  # Letters and numbers
        ("abc", True),  # Only letters
        ("123", True),  # Only numbers
        ("abc-123", False),  # Contains hyphen
        ("", False),  # Empty
        ("abc 123", False),  # Contains space
    ],
)
def test_text_is_alphanumeric(text: str, expected: bool) -> None:
    """Test text_is_alphanumeric() with various strings."""
    assert text_is_alphanumeric(text) == expected
