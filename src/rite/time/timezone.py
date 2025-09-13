# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Rite - Utilities - Timezone Module
==================================

This module provides the `Timezone` class for managing timezones using the
standard library `zoneinfo` module.

Supports:
- Converting datetime objects between timezones.
- Retrieving current time in a given timezone.
- Listing all available timezones.

Requires:
- Python 3.9+ (for `zoneinfo`)

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo, available_timezones

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================


class Timezone:
    """
    Timezone Class
    ==============


    Provides utilities for timezone management and conversion.
    """

    def __init__(
        self,
        timezone: str = "UTC",
    ) -> None:
        """
        Initialize with a specific timezone.
        """
        try:
            self.timezone = ZoneInfo(timezone)
        except Exception as exc:
            raise ValueError(f"Invalid timezone: {timezone}") from exc

    def convert(
        self,
        dt: datetime,
        target_timezone: str,
    ) -> datetime:
        """
        Convert a datetime object to a target timezone.
        """
        try:
            return dt.astimezone(ZoneInfo(target_timezone))
        except Exception as exc:
            raise ValueError(
                f"Invalid target timezone: {target_timezone}"
            ) from exc

    def now(self) -> datetime:
        """
        Get the current datetime in the handler's timezone.
        """
        return datetime.now(self.timezone)

    @staticmethod
    def list_timezones() -> List[str]:
        """
        List all available timezones (may vary by platform).
        """
        try:
            return sorted(available_timezones())
        except Exception as exc:
            # available_timezones is not available in Python < 3.9
            raise NotImplementedError(
                "Listing all timezones is not supported in this Python version."
            ) from exc

    def __str__(self) -> str:
        """
        String representation of the Timezone object.
        """
        return f"Current timezone: {self.timezone.key}"

    @staticmethod
    def get_timezone_from_abbreviation(abbreviation: str) -> str:
        """
        Return full timezone name from a common abbreviation.
        """
        timezone_map = {
            "PST": "America/Los_Angeles",
            "EST": "America/New_York",
            "CET": "Europe/Amsterdam",
            "UTC": "UTC",
        }
        if abbreviation not in timezone_map:
            raise ValueError(
                f"Unrecognized timezone abbreviation: {abbreviation}"
            )
        return timezone_map[abbreviation]


# =============================================================================
# Exports
# =============================================================================

__all__: List[str] = [
    "Timezone",
]


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Initialize the Timezone for UTC
    tz_handler = Timezone("UTC")
    print("Handler Timezone:", tz_handler)

    # Get the current time in UTC
    utc_now = tz_handler.now()
    print("Current UTC Time:", utc_now)

    # Convert UTC to another timezone
    local_time = tz_handler.convert(utc_now, "Europe/Amsterdam")
    print("Converted Time (Amsterdam):", local_time)

    # List all available timezones
    print(
        "Available Timezones:",
        # Display first 5 for brevity
        Timezone.list_timezones()[:5],
    )
