# -*- coding: utf-8 -*-

# =============================================================================
# Docstring
# =============================================================================

"""
Timezone Test Module
====================
This module tests the `Timezone` class, which provides functionalities for
managing and converting between timezones.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from datetime import datetime

# Import | Libraries
import pytest
import pytz

# Import | Local Modules
from rite.time.timezone import Timezone

# =============================================================================
# Test Cases
# =============================================================================


def test_initialization():
    """
    Test initialization of the `Timezone` class.
    """
    # Valid timezone
    tz = Timezone("Europe/Amsterdam")
    assert (
        tz.timezone.zone == "Europe/Amsterdam"
    ), "Timezone should initialize correctly."

    # Invalid timezone
    with pytest.raises(
        pytz.UnknownTimeZoneError, match="Invalid timezone: Invalid/Zone"
    ):
        Timezone("Invalid/Zone")


def test_convert():
    """
    Test conversion of a datetime object to a target timezone.
    """
    dt = datetime(2024, 12, 31, 23, 59, 59, tzinfo=pytz.UTC)
    tz = Timezone("UTC")

    # Convert to a valid timezone
    converted_dt = tz.convert(dt, "Europe/Amsterdam")
    assert (
        converted_dt.tzinfo.zone == "Europe/Amsterdam"
    ), "Conversion should update timezone."
    assert (
        converted_dt.hour == 0 or converted_dt.hour == 1
    ), "Conversion should adjust time correctly."

    # Convert to an invalid timezone
    with pytest.raises(pytz.UnknownTimeZoneError, match="Invalid/Zone"):
        tz.convert(dt, "Invalid/Zone")


def test_now():
    """
    Test retrieval of the current time in the handler's timezone.
    """
    tz = Timezone("UTC")
    now = tz.now()
    assert isinstance(
        now, datetime
    ), "Current time should be a datetime object."
    assert (
        now.tzinfo.zone == "UTC"
    ), "Timezone should match handler's timezone."


def test_list_timezones():
    """
    Test listing of all available timezones.
    """
    timezones = Timezone.list_timezones()
    assert isinstance(
        timezones, list
    ), "Timezones should be returned as a list."
    assert len(timezones) > 0, "List of timezones should not be empty."
    assert (
        "UTC" in timezones
    ), "UTC should be included in the list of timezones."


def test_get_timezone_from_abbreviation():
    """
    Test retrieval of full timezone name from abbreviation.
    """
    # Valid abbreviation
    assert (
        Timezone.get_timezone_from_abbreviation("PST") == "America/Los_Angeles"
    ), "Abbreviation should resolve correctly."
    assert (
        Timezone.get_timezone_from_abbreviation("EST") == "America/New_York"
    ), "Abbreviation should resolve correctly."

    # Invalid abbreviation
    with pytest.raises(
        ValueError, match="Unrecognized timezone abbreviation: XYZ"
    ):
        Timezone.get_timezone_from_abbreviation("XYZ")


def test_str_representation():
    """
    Test string representation of the `Timezone` class.
    """
    tz = Timezone("UTC")
    assert (
        str(tz) == "Current timezone: UTC"
    ), "String representation should match the timezone."


# =============================================================================
# Test Execution
# =============================================================================

if __name__ == "__main__":
    pytest.main()
