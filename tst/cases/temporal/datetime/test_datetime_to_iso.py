# =============================================================================
# Test: datetime_to_iso
# =============================================================================

"""
Tests for rite.temporal.datetime.datetime_to_iso.
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
from rite.temporal.datetime.datetime_to_iso import (
    datetime_to_iso,
)

# =============================================================================
# Imports
# =============================================================================


# =============================================================================
# Test Functions
# =============================================================================


class TestDatetimeToIso:
    """Tests for datetime_to_iso function."""

    def test_with_timezone_aware_datetime(self) -> None:
        """Test ISO format for timezone-aware datetime."""
        dt = datetime(2024, 12, 27, 15, 30, 45, tzinfo=timezone.utc)
        result = datetime_to_iso(dt)
        assert result == "2024-12-27T15:30:45+00:00"

    def test_with_naive_datetime(self) -> None:
        """Test ISO format for naive datetime."""
        dt = datetime(2024, 12, 27, 15, 30, 45)
        result = datetime_to_iso(dt)
        assert result == "2024-12-27T15:30:45"

    def test_format_structure(self) -> None:
        """Test that ISO format has correct structure."""
        dt = datetime(2024, 12, 27, 15, 30, 45, tzinfo=timezone.utc)
        result = datetime_to_iso(dt)
        # ISO format should contain T separator and timezone offset
        assert "T" in result
        assert "+" in result or "-" in result or result.endswith("Z")

    def test_epoch_datetime(self) -> None:
        """Test ISO format for epoch datetime."""
        dt = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        result = datetime_to_iso(dt)
        assert result == "1970-01-01T00:00:00+00:00"

    def test_with_microseconds(self) -> None:
        """Test ISO format with microseconds."""
        dt = datetime(2024, 12, 27, 15, 30, 45, 123456, tzinfo=timezone.utc)
        result = datetime_to_iso(dt)
        assert "123456" in result

    @pytest.mark.parametrize(
        "dt,expected_part",
        [
            (
                datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                "2024-01-01T00:00:00",
            ),
            (
                datetime(2024, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
                "2024-12-31T23:59:59",
            ),
            (
                datetime(2024, 6, 15, 12, 30, 45, tzinfo=timezone.utc),
                "2024-06-15T12:30:45",
            ),
        ],
    )
    def test_various_datetimes(self, dt: datetime, expected_part: str) -> None:
        """Test ISO format for various datetimes."""
        result = datetime_to_iso(dt)
        assert result.startswith(expected_part)

    def test_roundtrip_parsing(self) -> None:
        """Test that ISO format can be parsed back."""
        dt = datetime(2024, 12, 27, 15, 30, 45, tzinfo=timezone.utc)
        iso_str = datetime_to_iso(dt)
        # Should be parseable format
        assert datetime.fromisoformat(iso_str) == dt
