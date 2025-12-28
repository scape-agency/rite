# =============================================================================
# Test: duration_from_hours
# =============================================================================

"""
Tests for rite.temporal.duration.duration_from_hours.
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
from rite.temporal.duration.duration_from_hours import (
    duration_from_hours,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDurationFromHours:
    """Tests for duration_from_hours function."""

    def test_zero_hours(self) -> None:
        """Test with zero hours."""
        result = duration_from_hours(0)
        expected = timedelta(hours=0)
        assert result == expected

    def test_one_hour(self) -> None:
        """Test with one hour."""
        result = duration_from_hours(1)
        expected = timedelta(hours=1)
        assert result == expected

    def test_twenty_four_hours(self) -> None:
        """Test with 24 hours (one day)."""
        result = duration_from_hours(24)
        expected = timedelta(days=1)
        assert result == expected

    def test_fractional_hours(self) -> None:
        """Test with fractional hours."""
        result = duration_from_hours(1.5)
        expected = timedelta(hours=1.5)
        assert result == expected

    def test_forty_eight_hours(self) -> None:
        """Test with 48 hours (two days)."""
        result = duration_from_hours(48)
        assert result == timedelta(days=2)

    def test_returns_timedelta(self) -> None:
        """Test that result is timedelta object."""
        result = duration_from_hours(1)
        assert isinstance(result, timedelta)

    @pytest.mark.parametrize(
        "hours,expected_seconds",
        [
            (0, 0),
            (1, 3600),
            (2, 7200),
            (24, 86400),
            (48, 172800),
        ],
    )
    def test_various_hour_values(
        self, hours: int, expected_seconds: int
    ) -> None:
        """Test various hour values."""
        result = duration_from_hours(hours)
        assert result.total_seconds() == expected_seconds

    def test_large_hour_values(self) -> None:
        """Test with large hour values."""
        result = duration_from_hours(1000)
        assert result.total_seconds() == 3600000
