# =============================================================================
# Test: text_count
# =============================================================================

"""
Tests for rite.text.search.text_count.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.search.text_count import (
    text_count,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,substring,expected",
    [
        ("hello world", "o", 2),
        ("hello world", "l", 3),
        ("hello world", "world", 1),
        ("hello world", "foo", 0),
        ("aaa", "a", 3),
    ],
)
def test_text_count(text: str, substring: str, expected: int) -> None:
    """Test text_count() with various inputs."""
    assert text_count(text, substring) == expected
