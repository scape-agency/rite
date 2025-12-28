# =============================================================================
# Test: types_to_set
# =============================================================================

"""
Tests for rite.conversion.types.types_to_set.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_set import (
    types_to_set,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_types_to_set_basic_iterables() -> None:
    """Test conversion of iterables and scalars to set."""
    values = {1, 2, 3}
    assert types_to_set(values) is values

    assert types_to_set([1, 2, 2, 3]) == {1, 2, 3}
    assert types_to_set((1, 2, 3)) == {1, 2, 3}
    assert types_to_set("hello") == {"h", "e", "l", "o"}
    assert types_to_set(42) == {42}
