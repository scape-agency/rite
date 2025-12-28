# =============================================================================
# Test: timezone_convert
# =============================================================================

"""
Tests for rite.temporal.timezone.timezone_convert.
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
from rite.temporal.timezone.timezone_convert import (
    timezone_convert,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestTimezoneConvert:
    """Tests for timezone_convert function."""

    def test_utc_to_utc(self) -> None:
        """Test converting from UTC to UTC."""
        dt = datetime(2024, 12, 27, 12, 0, tzinfo=timezone.utc)
        result = timezone_convert(dt, "UTC")
        assert result.hour == 12
        assert result.tzinfo is not None

    def test_utc_to_newyork(self) -> None:
        """Test converting from UTC to America/New_York."""
        dt = datetime(2024, 12, 27, 12, 0, tzinfo=timezone.utc)
        result = timezone_convert(dt, "America/New_York")
        # UTC 12:00 is 7:00 AM EST
        assert result.hour == 7
        assert result.day == 27

    def test_utc_to_tokyo(self) -> None:
        """Test converting from UTC to Asia/Tokyo."""
        dt = datetime(2024, 12, 27, 12, 0, tzinfo=timezone.utc)
        result = timezone_convert(dt, "Asia/Tokyo")
        # UTC 12:00 is 21:00 JST (same day)
        assert result.hour == 21
        assert result.day == 27

    def test_utc_to_london(self) -> None:
        """Test converting from UTC to Europe/London."""
        dt = datetime(2024, 12, 27, 12, 0, tzinfo=timezone.utc)
        result = timezone_convert(dt, "Europe/London")
        # UTC 12:00 is 12:00 GMT (same in winter)
        assert result.hour == 12

    def test_midnight_utc_to_sydney(self) -> None:
        """Test midnight UTC conversion to Sydney."""
        dt = datetime(2024, 12, 27, 0, 0, tzinfo=timezone.utc)
        result = timezone_convert(dt, "Australia/Sydney")
        # UTC 00:00 is 11:00 AEDT same day (Sydney is UTC+11)
        assert result.hour == 11
        assert result.day == 27

    def test_timezone_offset_preserved(self) -> None:
        """Test that absolute time is preserved."""
        dt = datetime(2024, 12, 27, 12, 0, tzinfo=timezone.utc)
        result_ny = timezone_convert(dt, "America/New_York")
        result_tokyo = timezone_convert(dt, "Asia/Tokyo")
        # When converted back to timestamp, should be same time
        assert int(result_ny.timestamp()) == int(result_tokyo.timestamp())

    @pytest.mark.parametrize(
        "target_tz",
        [
            "UTC",
            "America/New_York",
            "Europe/London",
            "Asia/Tokyo",
            "Australia/Sydney",
        ],
    )
    def test_various_timezones(self, target_tz: str) -> None:
        """Test conversion to various timezones."""
        dt = datetime(2024, 12, 27, 12, 0, tzinfo=timezone.utc)
        result = timezone_convert(dt, target_tz)
        assert result.tzinfo is not None
        # Year, month should remain same (datetime representation may differ)
        assert result.year == 2024
