# =============================================================================
# Test: duration_from_minutes
# =============================================================================

"""
Tests for rite.temporal.duration.duration_from_minutes.
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
from rite.temporal.duration.duration_from_minutes import (
    duration_from_minutes,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDurationFromMinutes:
    """Tests for duration_from_minutes function."""

    def test_zero_minutes(self) -> None:
        """Test with zero minutes."""
        result = duration_from_minutes(0)
        expected = timedelta(minutes=0)
        assert result == expected

    def test_one_minute(self) -> None:
        """Test with one minute."""
        result = duration_from_minutes(1)
        expected = timedelta(minutes=1)
        assert result == expected

    def test_sixty_minutes(self) -> None:
        """Test with 60 minutes (one hour)."""
        result = duration_from_minutes(60)
        expected = timedelta(hours=1)
        assert result == expected

    def test_fractional_minutes(self) -> None:
        """Test with fractional minutes."""
        result = duration_from_minutes(1.5)
        # 1.5 minutes = 90 seconds
        assert result.total_seconds() == 90

    def test_1440_minutes(self) -> None:
        """Test with 1440 minutes (one day)."""
        result = duration_from_minutes(1440)
        assert result == timedelta(days=1)

    def test_returns_timedelta(self) -> None:
        """Test that result is timedelta object."""
        result = duration_from_minutes(1)
        assert isinstance(result, timedelta)

    @pytest.mark.parametrize(
        "minutes,expected_seconds",
        [
            (0, 0),
            (1, 60),
            (5, 300),
            (30, 1800),
            (60, 3600),
        ],
    )
    def test_various_minute_values(
        self, minutes: int, expected_seconds: int
    ) -> None:
        """Test various minute values."""
        result = duration_from_minutes(minutes)
        assert result.total_seconds() == expected_seconds

    def test_large_minute_values(self) -> None:
        """Test with large minute values."""
        result = duration_from_minutes(10000)
        assert result.total_seconds() == 600000
