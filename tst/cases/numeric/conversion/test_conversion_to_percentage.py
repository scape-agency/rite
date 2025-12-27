# =============================================================================
# Test: conversion_to_percentage
# =============================================================================

"""
Tests for rite.numeric.conversion.conversion_to_percentage.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.conversion.conversion_to_percentage import (
    conversion_to_percentage,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,decimals,expected",
    [
        (0.25, None, 25.0),
        (0.5, None, 50.0),
        (1.0, None, 100.0),
        (0.0, None, 0.0),
        (0.333, 1, 33.3),
    ],
)
def test_conversion_to_percentage(
    value: float, decimals: int | None, expected: float
) -> None:
    """Test conversion_to_percentage() with various inputs."""
    if decimals is None:
        assert conversion_to_percentage(value) == expected
    else:
        assert conversion_to_percentage(value, decimals) == expected
