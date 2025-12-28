# =============================================================================
# Test: types_to_percentage
# =============================================================================

"""
Tests for rite.conversion.types.types_to_percentage.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_percentage import (
    types_to_percentage,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, clamp, default, expected",
    [
        (None, True, None, None),
        (None, True, 0.0, 0.0),
        (35, True, None, 35.0),
        ("35", True, None, 35.0),
        ("35%", True, None, 35.0),
        (0.35, True, None, 35.0),
        (1.0, True, None, 100.0),
        (0.5, True, None, 50.0),
        (150, True, None, 100.0),
        (-10, True, None, 0.0),
        (150, False, None, 150.0),
        ("0.5", True, None, 50.0),
        ("invalid", True, None, None),
        ("invalid", True, 0.0, 0.0),
    ],
)
def test_types_to_percentage(
    value: object,
    clamp: bool,
    default: float | None,
    expected: float | None,
) -> None:
    """Test types_to_percentage() normalization and clamping behaviour."""
    assert types_to_percentage(value, default=default, clamp=clamp) == expected
