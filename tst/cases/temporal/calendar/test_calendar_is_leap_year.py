# =============================================================================
# Test: calendar_is_leap_year
# =============================================================================

"""
Tests for rite.temporal.calendar.calendar_is_leap_year.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.calendar.calendar_is_leap_year import (
    calendar_is_leap_year,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "year,expected",
    [
        (2024, True),  # Leap year (divisible by 4)
        (2023, False),  # Not a leap year
        (2000, True),  # Leap year (divisible by 400)
        (1900, False),  # Not a leap year (divisible by 100 but not 400)
        (2004, True),  # Leap year
        (2100, False),  # Not a leap year
    ],
)
def test_calendar_is_leap_year(year: int, expected: bool) -> None:
    """Test calendar_is_leap_year() with multiple years."""
    assert calendar_is_leap_year(year) == expected
