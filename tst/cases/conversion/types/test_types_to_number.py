# =============================================================================
# Test: types_to_number
# =============================================================================

"""
Tests for rite.conversion.types.types_to_number.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_number import (
    types_to_number,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, default, expected",
    [
        (None, None, None),
        (None, 0.0, 0.0),
        (10, None, 10.0),
        (3.5, None, 3.5),
        ("20", None, 20.0),
        (" 20 m", None, 20.0),
        ("45.5 %", None, 45.5),
        ("100/ha", None, 100.0),
        ("-2.5 kg", None, -2.5),
        ("1.5e3 m", None, 1500.0),
        ("invalid", None, None),
        ("invalid", 1.0, 1.0),
    ],
)
def test_types_to_number(
    value: object,
    default: float | None,
    expected: float | None,
) -> None:
    """Test types_to_number() parsing numeric prefixes from strings."""
    assert types_to_number(value, default) == expected
