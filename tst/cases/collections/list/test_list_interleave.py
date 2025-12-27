# =============================================================================
# Test: list_interleave
# =============================================================================

"""
Tests for rite.collections.list.list_interleave.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.list.list_interleave import (
    list_interleave,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_list_interleave() -> None:
    """Test list_interleave() with various inputs."""
    assert list_interleave([1, 2, 3], ["a", "b", "c"]) == [
        1,
        "a",
        2,
        "b",
        3,
        "c",
    ]
    assert list_interleave([1, 2], ["a", "b"]) == [1, "a", 2, "b"]
    assert list_interleave([1], [2], [3]) == [1, 2, 3]
    assert list_interleave([], []) == []
    # Note: zip stops at shortest list, so [1, 2, 3] with ["a"] gives [1, "a"]
    assert list_interleave([1, 2, 3], ["a"]) == [1, "a"]
