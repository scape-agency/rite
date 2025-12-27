# =============================================================================
# Test: conversion_from_percentage
# =============================================================================

"""
Tests for rite.numeric.conversion.conversion_from_percentage.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.conversion.conversion_from_percentage import (
    conversion_from_percentage,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        (25, 0.25),
        (50, 0.5),
        (100, 1.0),
        (0, 0.0),
        (75.5, 0.755),
    ],
)
def test_conversion_from_percentage(value: float, expected: float) -> None:
    """Test conversion_from_percentage() with various inputs."""
    assert conversion_from_percentage(value) == expected
