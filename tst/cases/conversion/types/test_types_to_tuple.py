# =============================================================================
# Test: types_to_tuple
# =============================================================================

"""
Tests for rite.conversion.types.types_to_tuple.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_tuple import (
    types_to_tuple,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_types_to_tuple_basic_iterables() -> None:
    """Test conversion of iterables and scalars to tuple."""
    values = (1, 2, 3)
    assert types_to_tuple(values) is values

    assert types_to_tuple([1, 2, 3]) == (1, 2, 3)

    result = types_to_tuple({1, 2, 3})
    assert sorted(result) == [1, 2, 3]

    assert types_to_tuple("hi") == ("h", "i")
    assert types_to_tuple(42) == (42,)

    # bytes are treated as a single value, not iterated
    data = b"ab"
    assert types_to_tuple(data) == (data,)
