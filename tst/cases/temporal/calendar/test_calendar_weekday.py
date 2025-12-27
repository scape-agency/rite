# =============================================================================
# Test: calendar_weekday
# =============================================================================

"""
Tests for rite.temporal.calendar.calendar_weekday.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.calendar.calendar_weekday import (
    calendar_weekday,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "year,month,day,expected",
    [
        (2024, 1, 1, 0),  # Monday
        (2024, 12, 27, 4),  # Friday
        (2024, 2, 29, 3),  # Thursday (leap year)
        (2024, 7, 4, 3),  # Thursday
        (2024, 12, 25, 2),  # Wednesday
    ],
)
def test_calendar_weekday(
    year: int, month: int, day: int, expected: int
) -> None:
    """Test calendar_weekday() with various dates."""
    assert calendar_weekday(year, month, day) == expected
