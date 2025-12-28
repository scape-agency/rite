# =============================================================================
# Test: range_in_range
# =============================================================================

"""
Tests for rite.numeric.range.range_in_range.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.range.range_in_range import (
    range_in_range,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, minimum, maximum, inclusive, expected",
    [
        (5, 0, 10, True, True),
        (0, 0, 10, True, True),
        (10, 0, 10, True, True),
        (0, 0, 10, False, False),
        (10, 0, 10, False, False),
        (5, 0, 10, False, True),
        (-1, 0, 10, True, False),
        (11, 0, 10, True, False),
    ],
)
def test_range_in_range(
    value: float,
    minimum: float,
    maximum: float,
    inclusive: bool,
    expected: bool,
) -> None:
    """Test inclusive and exclusive range membership."""
    assert range_in_range(value, minimum, maximum, inclusive) is expected
