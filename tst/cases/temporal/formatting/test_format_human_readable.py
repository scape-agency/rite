# =============================================================================
# Test: format_human_readable
# =============================================================================

"""
Tests for rite.temporal.formatting.format_human_readable.
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
from rite.temporal.formatting.format_human_readable import (
    format_human_readable,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestFormatHumanReadable:
    """Tests for format_human_readable function."""

    def test_basic_format(self) -> None:
        """Test basic human-readable format."""
        dt = datetime(2024, 12, 27, 15, 30)
        result = format_human_readable(dt)
        assert result == "December 27, 2024 at 03:30 PM"

    def test_morning_time(self) -> None:
        """Test format with morning time."""
        dt = datetime(2024, 12, 27, 9, 15)
        result = format_human_readable(dt)
        assert "December 27, 2024" in result
        assert "09:15 AM" in result

    def test_midnight(self) -> None:
        """Test format with midnight."""
        dt = datetime(2024, 12, 27, 0, 0)
        result = format_human_readable(dt)
        assert "December 27, 2024" in result
        assert "12:00 AM" in result

    def test_noon(self) -> None:
        """Test format with noon."""
        dt = datetime(2024, 12, 27, 12, 0)
        result = format_human_readable(dt)
        assert "December 27, 2024" in result
        assert "12:00 PM" in result

    def test_full_month_name(self) -> None:
        """Test that full month name is used."""
        dt = datetime(2024, 1, 1, 12, 0)
        result = format_human_readable(dt)
        assert "January" in result

    @pytest.mark.parametrize(
        "month,month_name",
        [
            (1, "January"),
            (6, "June"),
            (12, "December"),
        ],
    )
    def test_various_months(self, month: int, month_name: str) -> None:
        """Test format with various months."""
        dt = datetime(2024, month, 15, 12, 0)
        result = format_human_readable(dt)
        assert month_name in result

    def test_format_includes_year(self) -> None:
        """Test that year is included."""
        dt = datetime(2024, 12, 27, 15, 30)
        result = format_human_readable(dt)
        assert "2024" in result

    def test_twelve_hour_format(self) -> None:
        """Test that 12-hour format is used."""
        dt = datetime(2024, 12, 27, 20, 30)
        result = format_human_readable(dt)
        # 20:30 in 12-hour format is 8:30 PM
        assert "08:30 PM" in result
