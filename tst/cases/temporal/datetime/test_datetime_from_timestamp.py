# =============================================================================
# Test: datetime_from_timestamp
# =============================================================================

"""
Tests for rite.temporal.datetime.datetime_from_timestamp.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.datetime.datetime_from_timestamp import (
    datetime_from_timestamp,
)

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from datetime import datetime, timezone

# =============================================================================
# Test Functions
# =============================================================================


class TestDatetimeFromTimestamp:
    """Tests for datetime_from_timestamp function."""

    def test_epoch_timestamp(self) -> None:
        """Test with epoch timestamp (0)."""
        result = datetime_from_timestamp(0)
        expected = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        assert result == expected

    def test_specific_timestamp(self) -> None:
        """Test with specific timestamp."""
        # 2024-12-27 00:00:00 UTC
        result = datetime_from_timestamp(1735344000)
        assert result.year == 2024
        assert result.month == 12
        assert result.day == 27

    def test_recent_timestamp(self) -> None:
        """Test with timestamp from 2024."""
        # 2024-06-15 12:30:00 UTC
        result = datetime_from_timestamp(1718453400)
        assert result.year == 2024
        assert result.month == 6
        assert result.day == 15

    def test_float_timestamp(self) -> None:
        """Test with float timestamp for millisecond precision."""
        result = datetime_from_timestamp(1735344000.5)
        assert result.year == 2024
        assert result.microsecond == 500000

    def test_with_explicit_utc_timezone(self) -> None:
        """Test with explicit UTC timezone."""
        result = datetime_from_timestamp(1735344000, tz=timezone.utc)
        assert result.tzinfo == timezone.utc
        assert result.year == 2024

    def test_timezone_aware_result(self) -> None:
        """Test that result is timezone-aware."""
        result = datetime_from_timestamp(0)
        assert result.tzinfo is not None

    @pytest.mark.parametrize(
        "timestamp,year,month,day",
        [
            (0, 1970, 1, 1),
            (86400, 1970, 1, 2),  # One day after epoch
            (1735344000, 2024, 12, 27),
            (1735430400, 2024, 12, 28),
        ],
    )
    def test_various_timestamps(
        self, timestamp: int, year: int, month: int, day: int
    ) -> None:
        """Test various timestamp values."""
        result = datetime_from_timestamp(timestamp)
        assert result.year == year
        assert result.month == month
        assert result.day == day
