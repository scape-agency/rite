# =============================================================================
# Test: types_to_float
# =============================================================================

"""
Tests for rite.conversion.types.types_to_float.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_float import (
    types_to_float,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, default, expected",
    [
        (None, None, None),
        (None, 0.0, 0.0),
        (0, None, 0.0),
        (42, None, 42.0),
        (-7, None, -7.0),
        (3.14, None, 3.14),
        (True, None, 1.0),
        (False, None, 0.0),
        ("3.14", None, 3.14),
        ("  3.14  ", None, 3.14),
        ("1.5e3", None, 1500.0),
        ("  -2.5  ", None, -2.5),
        ("invalid", None, None),
        ("invalid", 1.5, 1.5),
    ],
)
def test_types_to_float(
    value: object,
    default: float | None,
    expected: float | None,
) -> None:
    """Test types_to_float() for numeric and string inputs."""
    assert types_to_float(value, default) == expected
