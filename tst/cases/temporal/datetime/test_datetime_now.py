# =============================================================================
# Test: datetime_now
# =============================================================================

"""
Tests for rite.temporal.datetime.datetime_now.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from datetime import datetime, timezone
import time

# Import | Local Modules
from rite.temporal.datetime.datetime_now import (
    datetime_now,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDatetimeNow:
    """Tests for datetime_now function."""

    def test_returns_datetime(self) -> None:
        """Test that function returns datetime object."""
        result = datetime_now()
        assert isinstance(result, datetime)

    def test_returns_timezone_aware(self) -> None:
        """Test that result is timezone-aware."""
        result = datetime_now()
        assert result.tzinfo is not None

    def test_returns_utc_by_default(self) -> None:
        """Test that result uses UTC timezone by default."""
        result = datetime_now()
        assert result.tzinfo == timezone.utc

    def test_current_time_is_reasonable(self) -> None:
        """Test that returned time is close to current time."""
        before = datetime.now(timezone.utc)
        result = datetime_now()
        after = datetime.now(timezone.utc)
        # Result should be between before and after
        assert before <= result <= after

    def test_with_explicit_utc(self) -> None:
        """Test with explicit UTC timezone parameter."""
        result = datetime_now(tz=timezone.utc)
        assert result.tzinfo == timezone.utc

    def test_monotonically_increasing(self) -> None:
        """Test that successive calls return increasing times."""
        time1 = datetime_now()
        time.sleep(0.01)  # Small delay
        time2 = datetime_now()
        assert time2 > time1

    def test_year_is_current(self) -> None:
        """Test that year is current or reasonable."""
        result = datetime_now()
        current_year = datetime.now(timezone.utc).year
        assert result.year == current_year
