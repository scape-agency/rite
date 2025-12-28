# =============================================================================
# Test: duration_to_seconds
# =============================================================================

"""
Tests for rite.temporal.duration.duration_to_seconds.
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
from rite.temporal.duration.duration_to_seconds import (
    duration_to_seconds,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDurationToSeconds:
    """Tests for duration_to_seconds function."""

    def test_zero_duration(self) -> None:
        """Test with zero duration."""
        td = timedelta(seconds=0)
        result = duration_to_seconds(td)
        assert result == 0.0

    def test_one_second(self) -> None:
        """Test with one second duration."""
        td = timedelta(seconds=1)
        result = duration_to_seconds(td)
        assert result == 1.0

    def test_one_minute(self) -> None:
        """Test with one minute duration."""
        td = timedelta(minutes=1)
        result = duration_to_seconds(td)
        assert result == 60.0

    def test_one_hour(self) -> None:
        """Test with one hour duration."""
        td = timedelta(hours=1)
        result = duration_to_seconds(td)
        assert result == 3600.0

    def test_one_day(self) -> None:
        """Test with one day duration."""
        td = timedelta(days=1)
        result = duration_to_seconds(td)
        assert result == 86400.0

    def test_returns_float(self) -> None:
        """Test that result is float type."""
        td = timedelta(seconds=1)
        result = duration_to_seconds(td)
        assert isinstance(result, float)

    def test_fractional_seconds(self) -> None:
        """Test with fractional seconds."""
        td = timedelta(seconds=1, microseconds=500000)
        result = duration_to_seconds(td)
        assert result == 1.5

    @pytest.mark.parametrize(
        "td,expected",
        [
            (timedelta(seconds=0), 0.0),
            (timedelta(seconds=1), 1.0),
            (timedelta(minutes=1), 60.0),
            (timedelta(hours=1), 3600.0),
            (timedelta(days=1), 86400.0),
        ],
    )
    def test_various_durations(self, td: timedelta, expected: float) -> None:
        """Test various duration values."""
        result = duration_to_seconds(td)
        assert result == expected

    def test_combined_units(self) -> None:
        """Test duration with combined time units."""
        td = timedelta(days=1, hours=2, minutes=30, seconds=45)
        result = duration_to_seconds(td)
        # 86400 + 7200 + 1800 + 45 = 95445
        assert result == 95445.0
