# =============================================================================
# Test: duration_from_seconds
# =============================================================================

"""
Tests for rite.temporal.duration.duration_from_seconds.
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
from rite.temporal.duration.duration_from_seconds import (
    duration_from_seconds,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDurationFromSeconds:
    """Tests for duration_from_seconds function."""

    def test_zero_seconds(self) -> None:
        """Test with zero seconds."""
        result = duration_from_seconds(0)
        expected = timedelta(seconds=0)
        assert result == expected

    def test_one_second(self) -> None:
        """Test with one second."""
        result = duration_from_seconds(1)
        expected = timedelta(seconds=1)
        assert result == expected

    def test_sixty_seconds(self) -> None:
        """Test with 60 seconds (one minute)."""
        result = duration_from_seconds(60)
        assert result == timedelta(minutes=1)

    def test_3600_seconds(self) -> None:
        """Test with 3600 seconds (one hour)."""
        result = duration_from_seconds(3600)
        assert result == timedelta(hours=1)

    def test_fractional_seconds(self) -> None:
        """Test with fractional seconds."""
        result = duration_from_seconds(90.5)
        assert result.total_seconds() == 90.5
        assert result.microseconds == 500000

    def test_returns_timedelta(self) -> None:
        """Test that result is timedelta object."""
        result = duration_from_seconds(1)
        assert isinstance(result, timedelta)

    @pytest.mark.parametrize(
        "seconds,expected_total",
        [
            (0, 0),
            (1, 1),
            (60, 60),
            (3600, 3600),
            (86400, 86400),
        ],
    )
    def test_various_second_values(
        self, seconds: int, expected_total: int
    ) -> None:
        """Test various second values."""
        result = duration_from_seconds(seconds)
        assert result.total_seconds() == expected_total

    def test_large_second_values(self) -> None:
        """Test with large second values."""
        result = duration_from_seconds(1000000)
        assert result.total_seconds() == 1000000
