# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Duration Test Module
====================

This module provides unit tests for the `Duration` class, covering:
- Initialization with default and specific values.
- String representation of durations.
- Conversion to/from days and seconds.
- Arithmetic operations (addition and subtraction).

Dependencies:
-------------
- pytest: A testing framework for running the test cases.

"""


# =============================================================================
# Import
# =============================================================================

# Import | Future
from __future__ import annotations


# Import | Standard Library
from datetime import timedelta

# Import | Libraries
import pytest

# Import | Local Modules
from rite.time.duration import Duration

# =============================================================================
# Test Cases
# =============================================================================


def test_duration_initialization():
    """
    Test initialization of Duration objects with default and specific values.
    """

    # Default initialization
    duration = Duration()
    assert duration.td == timedelta(seconds=0)

    # Initialization with specific seconds
    duration = Duration(3600)  # 1 hour
    assert duration.td == timedelta(seconds=3600)

    # Initialization with fractional seconds
    duration = Duration(3600.5)  # 1 hour and 0.5 seconds
    assert duration.td == timedelta(seconds=3600.5)


def test_duration_str():
    """
    Test string representation of Duration objects.
    """

    # Normal cases
    assert str(Duration(3661)) == "1h 1m 1s"  # 1 hour, 1 minute, 1 second
    assert str(Duration(59)) == "0h 0m 59s"  # 59 seconds
    assert str(Duration(3600 * 25)) == "25h 0m 0s"  # 25 hours

    # Edge case with zero seconds
    assert str(Duration(0)) == "0h 0m 0s"


def test_from_days():
    """
    Test creating Duration objects from days.
    """

    # Normal cases
    duration = Duration.from_days(1.5)  # 1.5 days
    assert duration.td == timedelta(days=1.5)

    # Edge case with 0 days
    duration = Duration.from_days(0)
    assert duration.td == timedelta(days=0)


def test_to_days():
    """
    Test converting Duration objects to days.
    """

    # Normal cases
    duration = Duration(86400 * 1.5)  # 1.5 days in seconds
    assert duration.to_days() == 1.5

    # Edge case with 0 seconds
    duration = Duration(0)
    assert duration.to_days() == 0.0


def test_add():
    """
    Test adding two Duration objects.
    """

    duration1 = Duration(3600)  # 1 hour
    duration2 = Duration(7200)  # 2 hours

    # Test addition
    result = duration1.add(duration2)
    assert result.td == timedelta(seconds=10800)  # 3 hours
    assert duration1.td == timedelta(seconds=10800)  # Original is updated


def test_subtract():
    """
    Test subtracting one Duration object from another.
    """

    duration1 = Duration(7200)  # 2 hours
    duration2 = Duration(3600)  # 1 hour

    # Test subtraction
    result = duration1.subtract(duration2)
    assert result.td == timedelta(seconds=3600)  # 1 hour
    assert duration1.td == timedelta(seconds=3600)  # Original is updated

    # Edge case: Subtracting larger duration
    duration1 = Duration(3600)  # 1 hour
    duration2 = Duration(7200)  # 2 hours
    result = duration1.subtract(duration2)
    assert result.td == timedelta(seconds=-3600)  # Negative duration


def test_to_seconds():
    """
    Test converting Duration objects to seconds.
    """

    # Normal cases
    duration = Duration(12345)
    assert duration.to_seconds() == 12345

    # Edge case with 0 seconds
    duration = Duration(0)
    assert duration.to_seconds() == 0.0


# =============================================================================
# Test Execution
# =============================================================================

if __name__ == "__main__":
    pytest.main()
