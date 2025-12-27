# =============================================================================
# Test: converter_string_to_decimal
# =============================================================================

"""
Tests for rite.text.converters.converter_string_to_decimal.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.converter_string_to_decimal import (
    convert_string_to_decimal,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,length,expected",
    [
        ("3.14159", 2, "3.14"),
        ("0.1", 3, "0.100"),
        ("100", 0, "100"),
        ("abc", 3, None),
        (None, 3, None),
        ("", 3, None),
    ],
)
def test_convert_string_to_decimal(
    value: str | None, length: int, expected: str | None
) -> None:
    """Test convert_string_to_decimal() with various inputs."""
    # Import | Standard Library
    from decimal import Decimal

    result = convert_string_to_decimal(value, length)
    if expected is None:
        assert result is None
    else:
        assert str(result) == expected
