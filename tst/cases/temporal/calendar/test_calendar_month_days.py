# =============================================================================
# Test: calendar_month_days
# =============================================================================

"""
Tests for rite.temporal.calendar.calendar_month_days.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.calendar.calendar_month_days import (
    calendar_month_days,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "year,month,expected",
    [
        (2024, 1, 31),  # January
        (2024, 2, 29),  # February (leap year)
        (2023, 2, 28),  # February (non-leap year)
        (2024, 4, 30),  # April
        (2024, 6, 30),  # June
        (2024, 12, 31),  # December
    ],
)
def test_calendar_month_days(year: int, month: int, expected: int) -> None:
    """Test calendar_month_days() with various months."""
    assert calendar_month_days(year, month) == expected
