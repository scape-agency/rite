# =============================================================================
# Test: to_number
# =============================================================================

"""
Tests for rite.conversion.to_number.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.to_number import to_number

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        (None, None),
        (10, 10.0),
        (3.5, 3.5),
        ("20", 20.0),
        (" 20 m", 20.0),
        ("45.5 %", 45.5),
        ("100/ha", 100.0),
        ("-2.5 kg", -2.5),
        ("invalid", None),
    ],
)
def test_to_number_parses_numeric_prefix(
    value: object, expected: float | None
) -> None:
    """Extract leading numeric part from plain and unit-suffixed strings."""
    assert to_number(value) == expected
