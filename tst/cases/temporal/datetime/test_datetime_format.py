# =============================================================================
# Test: datetime_format
# =============================================================================

"""
Tests for rite.temporal.datetime.datetime_format.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.datetime.datetime_format import (
    datetime_format,
)

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from datetime import datetime

# =============================================================================
# Test Functions
# =============================================================================


class TestDatetimeFormat:
    """Tests for datetime_format function."""

    def test_default_format(self) -> None:
        """Test default format string."""
        dt = datetime(2024, 12, 27, 15, 30, 45)
        result = datetime_format(dt)
        assert result == "2024-12-27 15:30:45"

    def test_custom_format_date_only(self) -> None:
        """Test custom format for date only."""
        dt = datetime(2024, 12, 27, 15, 30)
        result = datetime_format(dt, "%Y-%m-%d")
        assert result == "2024-12-27"

    def test_custom_format_time_only(self) -> None:
        """Test custom format for time only."""
        dt = datetime(2024, 12, 27, 15, 30, 45)
        result = datetime_format(dt, "%H:%M:%S")
        assert result == "15:30:45"

    @pytest.mark.parametrize(
        "dt,fmt,expected",
        [
            (
                datetime(2024, 1, 1, 0, 0, 0),
                "%Y-%m-%d",
                "2024-01-01",
            ),
            (
                datetime(2024, 12, 31, 23, 59, 59),
                "%d/%m/%Y",
                "31/12/2024",
            ),
            (
                datetime(2024, 6, 15, 14, 30),
                "%A, %B %d, %Y",
                "Saturday, June 15, 2024",
            ),
            (
                datetime(2024, 3, 10, 9, 5, 3),
                "%I:%M:%S %p",
                "09:05:03 AM",
            ),
        ],
    )
    def test_various_formats(
        self, dt: datetime, fmt: str, expected: str
    ) -> None:
        """Test various format strings."""
        result = datetime_format(dt, fmt)
        assert result == expected

    def test_iso_format(self) -> None:
        """Test ISO format."""
        dt = datetime(2024, 12, 27, 15, 30, 45)
        result = datetime_format(dt, "%Y-%m-%dT%H:%M:%S")
        assert result == "2024-12-27T15:30:45"
