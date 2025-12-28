# =============================================================================
# Test: timezone_list
# =============================================================================

"""
Tests for rite.temporal.timezone.timezone_list.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.temporal.timezone.timezone_list import (
    timezone_list,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestTimezoneList:
    """Tests for timezone_list function."""

    def test_returns_list(self) -> None:
        """Test that function returns a list."""
        result = timezone_list()
        assert isinstance(result, list)

    def test_list_not_empty(self) -> None:
        """Test that list is not empty."""
        result = timezone_list()
        assert len(result) > 0

    def test_contains_utc(self) -> None:
        """Test that UTC is in the list."""
        result = timezone_list()
        assert "UTC" in result

    def test_contains_common_timezones(self) -> None:
        """Test that common timezones are in the list."""
        result = timezone_list()
        common_zones = [
            "America/New_York",
            "Europe/London",
            "Asia/Tokyo",
            "Australia/Sydney",
        ]
        for zone in common_zones:
            assert zone in result

    def test_list_is_sorted(self) -> None:
        """Test that list is sorted."""
        result = timezone_list()
        assert result == sorted(result)

    def test_all_strings(self) -> None:
        """Test that all items in list are strings."""
        result = timezone_list()
        assert all(isinstance(item, str) for item in result)

    def test_no_duplicates(self) -> None:
        """Test that list contains no duplicates."""
        result = timezone_list()
        assert len(result) == len(set(result))

    @pytest.mark.parametrize(
        "zone_name",
        [
            "UTC",
            "GMT",
            "America/Los_Angeles",
            "America/New_York",
            "Europe/Paris",
            "Europe/London",
        ],
    )
    def test_contains_specific_zones(self, zone_name: str) -> None:
        """Test that specific timezones are in the list."""
        result = timezone_list()
        assert zone_name in result
