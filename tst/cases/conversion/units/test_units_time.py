# =============================================================================
# Test: units_time
# =============================================================================

"""
Tests for rite.conversion.units.units_time.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.units.units_time import (
    units_days_to_seconds,
    units_hours_to_minutes,
    units_hours_to_seconds,
    units_minutes_to_hours,
    units_minutes_to_seconds,
    units_seconds_to_days,
    units_seconds_to_hours,
    units_seconds_to_minutes,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "seconds,expected",
    [
        (60.0, 1.0),
        (120.0, 2.0),
    ],
)
def test_units_seconds_to_minutes(seconds: float, expected: float) -> None:
    """Convert seconds to minutes using simple division."""
    assert units_seconds_to_minutes(seconds) == expected


@pytest.mark.parametrize(
    "minutes,expected",
    [
        (1.0, 60.0),
        (2.0, 120.0),
    ],
)
def test_units_minutes_to_seconds(minutes: float, expected: float) -> None:
    """Convert minutes to seconds using multiplication by 60."""
    assert units_minutes_to_seconds(minutes) == expected


@pytest.mark.parametrize(
    "seconds,expected",
    [
        (3600.0, 1.0),
        (7200.0, 2.0),
    ],
)
def test_units_seconds_to_hours(seconds: float, expected: float) -> None:
    """Convert seconds to hours using documented examples."""
    assert units_seconds_to_hours(seconds) == expected


@pytest.mark.parametrize(
    "hours,expected",
    [
        (1.0, 3600.0),
        (2.0, 7200.0),
    ],
)
def test_units_hours_to_seconds(hours: float, expected: float) -> None:
    """Convert hours to seconds using multiplication by 3600."""
    assert units_hours_to_seconds(hours) == expected


@pytest.mark.parametrize(
    "seconds,expected",
    [
        (86400.0, 1.0),
        (172800.0, 2.0),
    ],
)
def test_units_seconds_to_days(seconds: float, expected: float) -> None:
    """Convert seconds to days using documented examples."""
    assert units_seconds_to_days(seconds) == expected


@pytest.mark.parametrize(
    "days,expected",
    [
        (1.0, 86400.0),
        (2.0, 172800.0),
    ],
)
def test_units_days_to_seconds(days: float, expected: float) -> None:
    """Convert days to seconds using multiplication by 86400."""
    assert units_days_to_seconds(days) == expected


@pytest.mark.parametrize(
    "minutes,expected",
    [
        (60.0, 1.0),
        (120.0, 2.0),
    ],
)
def test_units_minutes_to_hours(minutes: float, expected: float) -> None:
    """Convert minutes to hours using simple division."""
    assert units_minutes_to_hours(minutes) == expected


@pytest.mark.parametrize(
    "hours,expected",
    [
        (1.0, 60.0),
        (2.0, 120.0),
    ],
)
def test_units_hours_to_minutes(hours: float, expected: float) -> None:
    """Convert hours to minutes using multiplication by 60."""
    assert units_hours_to_minutes(hours) == expected
