# =============================================================================
# Test: datetime_to_timestamp
# =============================================================================

"""
Tests for rite.temporal.datetime.datetime_to_timestamp.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from datetime import datetime, timezone

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.datetime.datetime_to_timestamp import (
    datetime_to_timestamp,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDatetimeToTimestamp:
    """Tests for datetime_to_timestamp function."""

    def test_epoch_datetime(self) -> None:
        """Test timestamp for epoch datetime."""
        dt = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        result = datetime_to_timestamp(dt)
        assert result == 0

    def test_one_day_after_epoch(self) -> None:
        """Test timestamp one day after epoch."""
        dt = datetime(1970, 1, 2, 0, 0, 0, tzinfo=timezone.utc)
        result = datetime_to_timestamp(dt)
        assert result == 86400  # 24 * 60 * 60

    def test_recent_datetime(self) -> None:
        """Test timestamp for recent datetime."""
        dt = datetime(2024, 12, 27, 0, 0, 0, tzinfo=timezone.utc)
        result = datetime_to_timestamp(dt)
        # Should be a large positive number
        assert result > 0
        assert result > 1700000000

    def test_returns_integer(self) -> None:
        """Test that result is integer type."""
        dt = datetime(2024, 12, 27, 15, 30, 45, tzinfo=timezone.utc)
        result = datetime_to_timestamp(dt)
        assert isinstance(result, int)

    def test_microseconds_truncated(self) -> None:
        """Test that microseconds are truncated to seconds."""
        dt1 = datetime(2024, 12, 27, 15, 30, 45, 100000, tzinfo=timezone.utc)
        dt2 = datetime(2024, 12, 27, 15, 30, 45, 900000, tzinfo=timezone.utc)
        # Both should round down to same second
        result1 = datetime_to_timestamp(dt1)
        result2 = datetime_to_timestamp(dt2)
        assert result1 == result2

    @pytest.mark.parametrize(
        "year,month,day,expected_range",
        [
            (1970, 1, 1, (0, 1)),  # Epoch
            (1970, 1, 2, (86400, 86401)),  # One day after
            (2024, 12, 27, (1735257600, 1735257601)),  # Recent
        ],
    )
    def test_various_dates(
        self, year: int, month: int, day: int, expected_range: tuple[int, int]
    ) -> None:
        """Test timestamps for various dates."""
        dt = datetime(year, month, day, 0, 0, 0, tzinfo=timezone.utc)
        result = datetime_to_timestamp(dt)
        assert expected_range[0] <= result <= expected_range[1]

    def test_roundtrip_conversion(self) -> None:
        """Test conversion back and forth."""
        # Import | Local Modules
        from rite.temporal.datetime import datetime_from_timestamp

        dt_original = datetime(2024, 6, 15, 14, 30, 45, tzinfo=timezone.utc)
        timestamp = datetime_to_timestamp(dt_original)
        dt_recovered = datetime_from_timestamp(timestamp)
        # Timestamps lose microsecond precision
        assert dt_recovered.year == dt_original.year
        assert dt_recovered.month == dt_original.month
        assert dt_recovered.day == dt_original.day
        assert dt_recovered.hour == dt_original.hour
        assert dt_recovered.minute == dt_original.minute
        assert dt_recovered.second == dt_original.second
