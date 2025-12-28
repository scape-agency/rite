# =============================================================================
# Test: datetime_parse
# =============================================================================

"""
Tests for rite.temporal.datetime.datetime_parse.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from datetime import datetime

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.datetime.datetime_parse import (
    datetime_parse,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDatetimeParse:
    """Tests for datetime_parse function."""

    def test_default_format_parsing(self) -> None:
        """Test parsing with default format."""
        result = datetime_parse("2024-12-27 15:30:45")
        expected = datetime(2024, 12, 27, 15, 30, 45)
        assert result == expected

    def test_date_only_parsing(self) -> None:
        """Test parsing date only."""
        result = datetime_parse("2024-12-27", "%Y-%m-%d")
        expected = datetime(2024, 12, 27, 0, 0, 0)
        assert result == expected

    def test_time_only_parsing(self) -> None:
        """Test parsing time only."""
        result = datetime_parse("15:30:45", "%H:%M:%S")
        # Time without date defaults to 1900-01-01
        assert result.hour == 15
        assert result.minute == 30
        assert result.second == 45

    def test_iso_format_parsing(self) -> None:
        """Test parsing ISO format without timezone."""
        result = datetime_parse("2024-12-27T15:30:45", "%Y-%m-%dT%H:%M:%S")
        expected = datetime(2024, 12, 27, 15, 30, 45)
        assert result == expected

    def test_european_date_format(self) -> None:
        """Test parsing European date format."""
        result = datetime_parse("27/12/2024", "%d/%m/%Y")
        expected = datetime(2024, 12, 27, 0, 0, 0)
        assert result == expected

    def test_month_name_parsing(self) -> None:
        """Test parsing with full month name."""
        result = datetime_parse("December 27, 2024", "%B %d, %Y")
        expected = datetime(2024, 12, 27, 0, 0, 0)
        assert result == expected

    @pytest.mark.parametrize(
        "date_str,fmt,year,month,day",
        [
            ("2024-01-01 00:00:00", "%Y-%m-%d %H:%M:%S", 2024, 1, 1),
            ("31/12/2024", "%d/%m/%Y", 2024, 12, 31),
            (
                "June 15, 2024",
                "%B %d, %Y",
                2024,
                6,
                15,
            ),
            ("2024/06/15", "%Y/%m/%d", 2024, 6, 15),
        ],
    )
    def test_various_date_formats(
        self, date_str: str, fmt: str, year: int, month: int, day: int
    ) -> None:
        """Test parsing various date formats."""
        result = datetime_parse(date_str, fmt)
        assert result.year == year
        assert result.month == month
        assert result.day == day

    def test_returns_naive_datetime(self) -> None:
        """Test that parsed datetime is naive (no timezone)."""
        result = datetime_parse("2024-12-27 15:30:45")
        assert result.tzinfo is None
