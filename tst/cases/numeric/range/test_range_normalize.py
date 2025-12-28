# =============================================================================
# Test: range_normalize
# =============================================================================

"""
Tests for rite.numeric.range.range_normalize.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.range.range_normalize import (
    range_normalize,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, minimum, maximum, expected",
    [
        (5, 0, 10, 0.5),
        (0, 0, 10, 0.0),
        (10, 0, 10, 1.0),
        (5, 5, 5, 0.0),  # degenerate range
    ],
)
def test_range_normalize(
    value: float, minimum: float, maximum: float, expected: float
) -> None:
    """Test normalization to 0-1 including degenerate ranges."""
    assert range_normalize(value, minimum, maximum) == expected
