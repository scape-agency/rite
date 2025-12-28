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
def test_conversion_to_decimal(
    value,
    expected: str,
) -> None:
    """Test conversion_to_decimal() with various inputs."""
    result = conversion_to_decimal(value)
    assert str(result) == expected


def test_conversion_to_decimal_invalid() -> None:
    """Test conversion_to_decimal with invalid input (lines 58-59)."""
    result = conversion_to_decimal("not a number")
    assert result is None


def test_conversion_to_decimal_empty() -> None:
    """Test conversion_to_decimal with empty string."""
    result = conversion_to_decimal("")
    assert result is None
