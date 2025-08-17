# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Timestamp Test Module
=====================

This module tests the `Timestamp` class, which provides functionalities for
handling and manipulating timestamps, including conversion, formatting,
timezone adjustments, and duration operations.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from datetime import datetime, timedelta
from unittest.mock import patch

# Import | Libraries
import pytest

# Import | Local Modules
from rite.time.duration import Duration
from rite.time.timestamp import Timestamp
from rite.time.timezone import Timezone

# =============================================================================
# Test Cases
# =============================================================================


def test_initialization():
    """
    Test initialization of the `Timestamp` class.
    """
    # Default initialization
    ts = Timestamp()
    assert isinstance(
        ts.datetime, datetime
    ), "Timestamp should initialize with a datetime object."
    assert (
        ts.timezone.timezone.zone == "UTC"
    ), "Default timezone should be UTC."

    # Initialization with custom datetime and timezone
    custom_dt = datetime(2024, 12, 31, 23, 59, 59)
    ts_custom = Timestamp(custom_dt, "Europe/Amsterdam")
    expected_dt = custom_dt.astimezone(Timezone("Europe/Amsterdam").timezone)
    assert (
        ts_custom.datetime == expected_dt
    ), "Custom datetime should be correctly timezone-adjusted."
    assert (
        ts_custom.timezone.timezone.zone == "Europe/Amsterdam"
    ), "Custom timezone should match input."


def test_to_unix():
    """
    Test conversion of a `Timestamp` to UNIX time.
    """
    ts = Timestamp(
        datetime(2024, 12, 31, 23, 59, 59, tzinfo=Timezone("UTC").timezone),
        "UTC",
    )
    assert (
        ts.to_unix() == 1735689599
    ), "UNIX time conversion should match expected value."


def test_from_unix():
    """
    Test creation of a `Timestamp` from a UNIX timestamp.
    """
    ts = Timestamp.from_unix(1735689599, "UTC")
    expected_dt = datetime(
        2024, 12, 31, 23, 59, 59, tzinfo=Timezone("UTC").timezone
    )
    assert (
        ts.datetime == expected_dt
    ), "Timestamp should correctly interpret UNIX time."

    ts_tz = Timestamp.from_unix(1735689599, "Europe/Amsterdam")
    assert (
        ts_tz.timezone.timezone.zone == "Europe/Amsterdam"
    ), "Timezone should match input."


def test_parse():
    """
    Test parsing of a date string into a `Timestamp`.
    """
    # Parse in UTC
    ts = Timestamp.parse(
        "2024-12-31 23:59:59", fmt="%Y-%m-%d %H:%M:%S", tz="UTC"
    )
    expected_dt = datetime(
        2024, 12, 31, 23, 59, 59, tzinfo=Timezone("UTC").timezone
    )
    assert (
        ts.datetime == expected_dt
    ), "Parsed datetime should match expected value."

    # Parse in Europe/Amsterdam timezone
    # ts_tz = Timestamp.parse(
    #     "2024-12-31 23:59:59", fmt="%Y-%m-%d %H:%M:%S", tz="Europe/Amsterdam"
    # )
    # amsterdam_tz = Timezone("Europe/Amsterdam").timezone

    # # Use localize to correctly attach the timezone
    # naive_dt = datetime(2024, 12, 31, 23, 59, 59)
    # expected_dt_tz = amsterdam_tz.localize(naive_dt)

    # assert (
    #     ts_tz.datetime == expected_dt_tz
    # ), f"Expected {expected_dt_tz}, but got {ts_tz.datetime}"


def test_add_and_subtract_duration():
    """
    Test adding and subtracting durations to/from a `Timestamp`.
    """
    ts = Timestamp(datetime(2024, 12, 31, 23, 59, 59), "UTC")
    duration = Duration(seconds=3600)  # 1 hour

    ts_add = ts.add_duration_immutable(duration)
    assert ts_add.datetime == ts.datetime + timedelta(
        seconds=3600
    ), "Duration addition should be correct."

    ts_subtract = ts.subtract_duration_immutable(duration)
    assert ts_subtract.datetime == ts.datetime - timedelta(
        seconds=3600
    ), "Duration subtraction should be correct."


def test_difference():
    """
    Test calculation of difference between two `Timestamp` objects.
    """
    ts1 = Timestamp(datetime(2024, 12, 31, 23, 59, 59), "UTC")
    ts2 = Timestamp(datetime(2024, 12, 31, 22, 59, 59), "UTC")

    diff = ts1.difference(ts2)
    assert (
        diff.to_seconds() == 3600
    ), "Difference between timestamps should match expected value."


def test_to_iso8601():
    """
    Test conversion of a `Timestamp` to ISO 8601 format.
    """
    ts = Timestamp(
        datetime(2024, 12, 31, 23, 59, 59, tzinfo=Timezone("UTC").timezone),
        "UTC",
    )
    assert (
        ts.to_iso8601() == "2024-12-31T23:59:59+00:00"
    ), "ISO 8601 conversion should be correct."


def test_convert_to_timezone():
    """
    Test conversion of a `Timestamp` to a different timezone.
    """
    ts = Timestamp(
        datetime(2024, 12, 31, 23, 59, 59, tzinfo=Timezone("UTC").timezone),
        "UTC",
    )
    ts_converted = ts.convert_to_timezone("Europe/Amsterdam")

    # Verify the converted timezone
    assert (
        ts_converted.timezone.timezone.zone == "Europe/Amsterdam"
    ), "Converted timezone should match input."

    # Verify the converted datetime differs logically (offset is applied)
    assert (
        ts_converted.datetime.isoformat() != ts.datetime.isoformat()
    ), "Converted datetime ISO format should differ due to timezone offset."

    # Verify the expected converted time
    expected_converted_time = Timezone("Europe/Amsterdam").timezone.localize(
        datetime(2025, 1, 1, 0, 59, 59)
    )
    assert (
        ts_converted.datetime == expected_converted_time
    ), "Converted datetime should match the expected value."


@patch("sense.core.time.timestamp.datetime", autospec=True)
def test_current_time(mock_datetime):
    """
    Test initialization of `Timestamp` with the current time.
    """
    mock_now = datetime(
        2024, 12, 31, 23, 59, 59, tzinfo=Timezone("UTC").timezone
    )
    mock_datetime.now.return_value = mock_now

    ts = Timestamp()
    assert (
        ts.datetime == mock_now
    ), "Current time should match the mocked time."


# =============================================================================
# Test Execution
# =============================================================================

if __name__ == "__main__":
    pytest.main()
