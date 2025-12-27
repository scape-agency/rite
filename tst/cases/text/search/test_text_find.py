# =============================================================================
# Test: text_find
# =============================================================================

"""
Tests for rite.text.search.text_find.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.search.text_find import (
    text_find,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,substring,expected",
    [
        ("hello world", "world", 6),
        ("hello world", "hello", 0),
        ("hello world", "o", 4),
        ("hello world", "foo", -1),
        ("hello", "", 0),
    ],
)
def test_text_find(
    text: str, substring: str, expected: int
) -> None:
    """Test text_find() with various inputs."""
    assert text_find(text, substring) == expected
