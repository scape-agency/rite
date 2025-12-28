# =============================================================================
# Test: partial_right
# =============================================================================

"""
Tests for rite.functional.partial.partial_right.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.partial.partial_right import (
    partial_right,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_partial_right() -> None:
    """partial_right should fix arguments from the right side."""

    def subtract(x: int, y: int, z: int) -> int:
        return x - y - z

    f = partial_right(subtract, 5, 2)
    assert f(10) == 3
