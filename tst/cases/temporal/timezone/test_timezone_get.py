# =============================================================================
# Test: timezone_get
# =============================================================================

"""
Tests for rite.temporal.timezone.timezone_get.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.timezone.timezone_get import (
    timezone_get,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestTimezoneGet:
    """Tests for timezone_get function."""

    def test_utc_default(self) -> None:
        """Test getting UTC timezone by default."""
        result = timezone_get()
        assert isinstance(result, ZoneInfo)
        assert result.key == "UTC"

    def test_utc_explicit(self) -> None:
        """Test getting UTC timezone explicitly."""
        result = timezone_get("UTC")
        assert isinstance(result, ZoneInfo)
        assert result.key == "UTC"

    def test_new_york_timezone(self) -> None:
        """Test getting America/New_York timezone."""
        result = timezone_get("America/New_York")
        assert isinstance(result, ZoneInfo)
        assert result.key == "America/New_York"

    def test_tokyo_timezone(self) -> None:
        """Test getting Asia/Tokyo timezone."""
        result = timezone_get("Asia/Tokyo")
        assert isinstance(result, ZoneInfo)
        assert result.key == "Asia/Tokyo"

    def test_sydney_timezone(self) -> None:
        """Test getting Australia/Sydney timezone."""
        result = timezone_get("Australia/Sydney")
        assert isinstance(result, ZoneInfo)
        assert result.key == "Australia/Sydney"

    def test_london_timezone(self) -> None:
        """Test getting Europe/London timezone."""
        result = timezone_get("Europe/London")
        assert isinstance(result, ZoneInfo)
        assert result.key == "Europe/London"

    def test_invalid_timezone_raises_error(self) -> None:
        """Test that invalid timezone raises error."""
        with pytest.raises(ZoneInfoNotFoundError):
            timezone_get("Invalid/Timezone")

    @pytest.mark.parametrize(
        "tz_name",
        [
            "UTC",
            "GMT",
            "America/Los_Angeles",
            "America/Chicago",
            "Europe/Paris",
            "Africa/Cairo",
            "Asia/Shanghai",
            "Pacific/Auckland",
        ],
    )
    def test_various_timezones(self, tz_name: str) -> None:
        """Test getting various valid timezones."""
        result = timezone_get(tz_name)
        assert isinstance(result, ZoneInfo)
        assert result.key == tz_name
