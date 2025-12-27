# =============================================================================
# Test: text_ends_with
# =============================================================================

"""
Tests for rite.text.search.text_ends_with.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.search.text_ends_with import (
    text_ends_with,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,suffix,expected",
    [
        ("hello world", "world", True),
        ("hello world", "hello", False),
        ("hello world", "", True),
        ("hello world", "hello world", True),
        ("hello", "HELLO", False),  # Case-sensitive
    ],
)
def test_text_ends_with(
    text: str, suffix: str, expected: bool
) -> None:
    """Test text_ends_with() with various inputs."""
    assert text_ends_with(text, suffix) == expected
