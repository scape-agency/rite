# =============================================================================
# Test: text_starts_with
# =============================================================================

"""
Tests for rite.text.search.text_starts_with.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.search.text_starts_with import (
    text_starts_with,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,prefix,expected",
    [
        ("hello world", "hello", True),
        ("hello world", "world", False),
        ("hello world", "", True),
        ("hello world", "hello world", True),
        ("hello", "HELLO", False),  # Case-sensitive
    ],
)
def test_text_starts_with(text: str, prefix: str, expected: bool) -> None:
    """Test text_starts_with() with various inputs."""
    assert text_starts_with(text, prefix) == expected
