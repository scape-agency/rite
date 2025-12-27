# =============================================================================
# Test: text_contains
# =============================================================================

"""
Tests for rite.text.search.text_contains.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.search.text_contains import (
    text_contains,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,substring,expected",
    [
        ("hello world", "world", True),
        ("hello world", "foo", False),
        ("hello world", "hello", True),
        ("hello world", "", True),
        ("test", "TEST", False),  # Case-sensitive
    ],
)
def test_text_contains(text: str, substring: str, expected: bool) -> None:
    """Test text_contains() with various inputs."""
    assert text_contains(text, substring) == expected
