# =============================================================================
# Test: units_weight
# =============================================================================

"""
Tests for rite.conversion.units.units_weight.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.units.units_weight import (
    units_grams_to_kilograms,
    units_grams_to_ounces,
    units_grams_to_pounds,
    units_kilograms_to_grams,
    units_ounces_to_grams,
    units_pounds_to_grams,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "grams,expected",
    [
        (1000.0, 1.0),
        (500.0, 0.5),
    ],
)
def test_units_grams_to_kilograms(grams: float, expected: float) -> None:
    """Convert grams to kilograms using division by 1000."""
    assert units_grams_to_kilograms(grams) == expected


@pytest.mark.parametrize(
    "kilograms,expected",
    [
        (1.0, 1000.0),
        (0.5, 500.0),
    ],
)
def test_units_kilograms_to_grams(kilograms: float, expected: float) -> None:
    """Convert kilograms to grams using multiplication by 1000."""
    assert units_kilograms_to_grams(kilograms) == expected


@pytest.mark.parametrize(
    "grams,expected",
    [
        (453.592, 1.0),
        (1000.0, 2.2),
    ],
)
def test_units_grams_to_pounds(grams: float, expected: float) -> None:
    """Convert grams to pounds using documented examples."""
    assert units_grams_to_pounds(grams) == pytest.approx(expected, rel=1e-2)


@pytest.mark.parametrize(
    "pounds,expected",
    [
        (1.0, 453.592),
        (2.2, 997.9),
    ],
)
def test_units_pounds_to_grams(pounds: float, expected: float) -> None:
    """Convert pounds to grams using documented factor."""
    assert units_pounds_to_grams(pounds) == pytest.approx(expected, rel=1e-2)


@pytest.mark.parametrize(
    "grams,expected",
    [
        (28.3495, 1.0),
        (100.0, 3.53),
    ],
)
def test_units_grams_to_ounces(grams: float, expected: float) -> None:
    """Convert grams to ounces using documented examples."""
    assert units_grams_to_ounces(grams) == pytest.approx(expected, rel=1e-2)


@pytest.mark.parametrize(
    "ounces,expected",
    [
        (1.0, 28.3495),
        (10.0, 283.5),
    ],
)
def test_units_ounces_to_grams(ounces: float, expected: float) -> None:
    """Convert ounces to grams using documented factor."""
    assert units_ounces_to_grams(ounces) == pytest.approx(expected, rel=1e-2)
