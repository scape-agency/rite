# =============================================================================
# Test: text_is_alpha
# =============================================================================

"""
Tests for rite.text.validation.text_is_alpha.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.validation.text_is_alpha import (
    text_is_alpha,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,expected",
    [
        ("abc", True),         # All letters
        ("ABC", True),         # Uppercase
        ("abc123", False),     # Contains numbers
        ("abc-def", False),    # Contains hyphen
        ("", False),           # Empty
        ("hello world", False), # Contains space
    ],
)
def test_text_is_alpha(text: str, expected: bool) -> None:
    """Test text_is_alpha() with various strings."""
    assert text_is_alpha(text) == expected
