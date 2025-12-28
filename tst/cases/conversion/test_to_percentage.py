# =============================================================================
# Test: to_percentage
# =============================================================================

"""
Tests for rite.conversion.to_percentage.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.to_percentage import to_percentage

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        (None, None),
        (35, 35.0),
        (0, 0.0),
        (100, 100.0),
        (150, 100.0),
        (-10, 0.0),
        (0.35, 35.0),
        (1.0, 100.0),
        ("35", 35.0),
        ("35%", 35.0),
        ("0.5", 50.0),
        ("150", 100.0),
        ("-10", 0.0),
        ("invalid", None),
    ],
)
def test_to_percentage_normalizes_and_clamps(
    value: object, expected: float | None
) -> None:
    """Handle numeric and string inputs, fractions, and clamping."""
    assert to_percentage(value) == expected
