# =============================================================================
# Test: duration_from_days
# =============================================================================

"""
Tests for rite.temporal.duration.duration_from_days.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from datetime import timedelta

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.duration.duration_from_days import (
    duration_from_days,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDurationFromDays:
    """Tests for duration_from_days function."""

    def test_zero_days(self) -> None:
        """Test with zero days."""
        result = duration_from_days(0)
        expected = timedelta(days=0)
        assert result == expected

    def test_one_day(self) -> None:
        """Test with one day."""
        result = duration_from_days(1)
        expected = timedelta(days=1)
        assert result == expected

    def test_seven_days(self) -> None:
        """Test with seven days (one week)."""
        result = duration_from_days(7)
        expected = timedelta(days=7)
        assert result == expected

    def test_fractional_days(self) -> None:
        """Test with fractional days."""
        result = duration_from_days(1.5)
        expected = timedelta(days=1, seconds=43200)  # 1.5 days
        assert result == expected

    def test_large_number_of_days(self) -> None:
        """Test with large number of days."""
        result = duration_from_days(365)
        assert result.days == 365

    def test_returns_timedelta(self) -> None:
        """Test that result is timedelta object."""
        result = duration_from_days(1)
        assert isinstance(result, timedelta)

    @pytest.mark.parametrize(
        "days,expected_days",
        [
            (0, 0),
            (1, 1),
            (7, 7),
            (30, 30),
            (365, 365),
        ],
    )
    def test_various_day_values(self, days: int, expected_days: int) -> None:
        """Test various day values."""
        result = duration_from_days(days)
        assert result.days == expected_days

    def test_float_days_precision(self) -> None:
        """Test float days are converted correctly."""
        result = duration_from_days(2.5)
        # 2.5 days = 2 days + 12 hours = 2 days + 43200 seconds
        assert result.days == 2
        assert result.seconds == 43200
