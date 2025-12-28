# =============================================================================
# Test: format_iso8601
# =============================================================================

"""
Tests for rite.temporal.formatting.format_iso8601.
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
from rite.temporal.formatting.format_iso8601 import (
    format_iso8601,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestFormatIso8601:
    """Tests for format_iso8601 function."""

    def test_with_timezone_aware(self) -> None:
        """Test ISO8601 format with timezone-aware datetime."""
        dt = datetime(2024, 12, 27, 15, 30, 45, tzinfo=timezone.utc)
        result = format_iso8601(dt)
        assert result == "2024-12-27T15:30:45+00:00"

    def test_with_naive_datetime(self) -> None:
        """Test ISO8601 format with naive datetime."""
        dt = datetime(2024, 12, 27, 15, 30, 45)
        result = format_iso8601(dt)
        assert result == "2024-12-27T15:30:45"

    def test_includes_t_separator(self) -> None:
        """Test that format includes T separator."""
        dt = datetime(2024, 12, 27, 15, 30, 45, tzinfo=timezone.utc)
        result = format_iso8601(dt)
        assert "T" in result

    def test_includes_timezone_offset(self) -> None:
        """Test that format includes timezone offset."""
        dt = datetime(2024, 12, 27, 15, 30, 45, tzinfo=timezone.utc)
        result = format_iso8601(dt)
        assert "+00:00" in result

    def test_epoch_datetime(self) -> None:
        """Test ISO8601 format for epoch."""
        dt = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        result = format_iso8601(dt)
        assert result == "1970-01-01T00:00:00+00:00"

    def test_with_microseconds(self) -> None:
        """Test ISO8601 format with microseconds."""
        dt = datetime(2024, 12, 27, 15, 30, 45, 123456, tzinfo=timezone.utc)
        result = format_iso8601(dt)
        assert "123456" in result

    @pytest.mark.parametrize(
        "dt,expected_part",
        [
            (
                datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                "2024-01-01T00:00:00",
            ),
            (
                datetime(2024, 6, 15, 12, 30, 45, tzinfo=timezone.utc),
                "2024-06-15T12:30:45",
            ),
            (
                datetime(2024, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                "2024-12-31T23:59:59",
            ),
        ],
    )
    def test_various_datetimes(self, dt: datetime, expected_part: str) -> None:
        """Test ISO8601 format for various datetimes."""
        result = format_iso8601(dt)
        assert result.startswith(expected_part)
