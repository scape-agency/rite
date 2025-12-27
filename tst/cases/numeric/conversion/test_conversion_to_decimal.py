# =============================================================================
# Test: conversion_to_decimal
# =============================================================================

"""
Tests for rite.numeric.conversion.conversion_to_decimal.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.conversion.conversion_to_decimal import (
    conversion_to_decimal,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        ("3.14", "3.14"),
        (3, "3"),
        (3.14, "3.14"),
        ("0", "0"),
        (0, "0"),
    ],
)
def test_conversion_to_decimal(value, expected: str) -> None:
    """Test conversion_to_decimal() with various inputs."""
    # Import | Standard Library
    from decimal import Decimal

    result = conversion_to_decimal(value)
    assert str(result) == expected
