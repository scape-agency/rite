# =============================================================================
# Test: units_length
# =============================================================================

"""
Tests for rite.conversion.units.units_length.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.units.units_length import (
    units_feet_to_meters,
    units_inches_to_meters,
    units_kilometers_to_meters,
    units_meters_to_feet,
    units_meters_to_inches,
    units_meters_to_kilometers,
    units_meters_to_miles,
    units_miles_to_meters,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "meters,expected",
    [
        (1.0, 3.28084),
        (10.0, 32.8084),
    ],
)
def test_units_meters_to_feet(meters: float, expected: float) -> None:
    """Convert meters to feet using documented factor."""
    assert units_meters_to_feet(meters) == pytest.approx(expected)


@pytest.mark.parametrize(
    "feet,expected",
    [
        (3.28084, 1.0),
        (10.0, pytest.approx(3.05, rel=1e-2)),
    ],
)
def test_units_feet_to_meters(feet: float, expected: float) -> None:
    """Invert meters↔feet conversion within reasonable precision."""
    assert units_feet_to_meters(feet) == pytest.approx(expected, rel=1e-2)


@pytest.mark.parametrize(
    "meters,expected",
    [
        (1.0, 39.3701),
        (0.1, 3.93701),
    ],
)
def test_units_meters_to_inches(meters: float, expected: float) -> None:
    """Convert meters to inches using documented factor."""
    assert units_meters_to_inches(meters) == pytest.approx(expected)


@pytest.mark.parametrize(
    "inches,expected",
    [
        (39.3701, 1.0),
        (10.0, 0.25),
    ],
)
def test_units_inches_to_meters(inches: float, expected: float) -> None:
    """Invert meters↔inches conversion using documented examples."""
    assert units_inches_to_meters(inches) == pytest.approx(expected, rel=5e-2)


@pytest.mark.parametrize(
    "meters,expected",
    [
        (1000.0, 1.0),
        (500.0, 0.5),
    ],
)
def test_units_meters_to_kilometers(meters: float, expected: float) -> None:
    """Convert meters to kilometers exactly via division by 1000."""
    assert units_meters_to_kilometers(meters) == expected


@pytest.mark.parametrize(
    "kilometers,expected",
    [
        (1.0, 1000.0),
        (0.5, 500.0),
    ],
)
def test_units_kilometers_to_meters(
    kilometers: float, expected: float
) -> None:
    """Convert kilometers to meters exactly via multiplication by 1000."""
    assert units_kilometers_to_meters(kilometers) == expected


@pytest.mark.parametrize(
    "meters,expected",
    [
        (1609.34, 1.0),
        (1000.0, 0.62),
    ],
)
def test_units_meters_to_miles(meters: float, expected: float) -> None:
    """Convert meters to miles using documented examples."""
    assert units_meters_to_miles(meters) == pytest.approx(expected, rel=1e-2)


@pytest.mark.parametrize(
    "miles,expected",
    [
        (1.0, 1609.34),
        (10.0, 16093.4),
    ],
)
def test_units_miles_to_meters(miles: float, expected: float) -> None:
    """Convert miles to meters using documented factor."""
    assert units_miles_to_meters(miles) == pytest.approx(expected, rel=1e-2)
