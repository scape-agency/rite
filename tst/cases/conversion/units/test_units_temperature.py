# =============================================================================
# Test: units_temperature
# =============================================================================

"""
Tests for rite.conversion.units.units_temperature.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.units.units_temperature import (
    units_celsius_to_fahrenheit,
    units_celsius_to_kelvin,
    units_fahrenheit_to_celsius,
    units_fahrenheit_to_kelvin,
    units_kelvin_to_celsius,
    units_kelvin_to_fahrenheit,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "celsius,expected",
    [
        (0.0, 32.0),
        (100.0, 212.0),
        (-40.0, -40.0),
    ],
)
def test_units_celsius_to_fahrenheit(celsius: float, expected: float) -> None:
    """Convert Celsius to Fahrenheit using documented identity points."""
    assert units_celsius_to_fahrenheit(celsius) == expected


@pytest.mark.parametrize(
    "fahrenheit,expected",
    [
        (32.0, 0.0),
        (212.0, 100.0),
        (-40.0, -40.0),
    ],
)
def test_units_fahrenheit_to_celsius(
    fahrenheit: float, expected: float
) -> None:
    """Convert Fahrenheit to Celsius using documented identity points."""
    assert units_fahrenheit_to_celsius(fahrenheit) == expected


@pytest.mark.parametrize(
    "celsius,expected",
    [
        (0.0, 273.15),
        (100.0, 373.15),
        (-273.15, 0.0),
    ],
)
def test_units_celsius_to_kelvin(celsius: float, expected: float) -> None:
    """Convert Celsius to Kelvin using documented examples."""
    assert units_celsius_to_kelvin(celsius) == pytest.approx(expected)


@pytest.mark.parametrize(
    "kelvin,expected",
    [
        (273.15, 0.0),
        (373.15, 100.0),
        (0.0, -273.15),
    ],
)
def test_units_kelvin_to_celsius(kelvin: float, expected: float) -> None:
    """Convert Kelvin to Celsius using documented examples."""
    assert units_kelvin_to_celsius(kelvin) == pytest.approx(expected)


@pytest.mark.parametrize(
    "fahrenheit,expected",
    [
        (32.0, 273.15),
        (212.0, 373.15),
    ],
)
def test_units_fahrenheit_to_kelvin(
    fahrenheit: float, expected: float
) -> None:
    """Convert Fahrenheit to Kelvin via Celsius step."""
    assert units_fahrenheit_to_kelvin(fahrenheit) == pytest.approx(expected)


@pytest.mark.parametrize(
    "kelvin,expected",
    [
        (273.15, 32.0),
        (373.15, 212.0),
    ],
)
def test_units_kelvin_to_fahrenheit(kelvin: float, expected: float) -> None:
    """Convert Kelvin to Fahrenheit via Celsius step."""
    assert units_kelvin_to_fahrenheit(kelvin) == pytest.approx(expected)
