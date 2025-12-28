# =============================================================================
# Test: types_to_int
# =============================================================================

"""
Tests for rite.conversion.types.types_to_int.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_int import (
    types_to_int,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, default, expected",
    [
        (None, None, None),
        (None, 0, 0),
        (0, None, 0),
        (42, None, 42),
        (-7, None, -7),
        (3.14, None, 3),
        (True, None, 1),
        (False, None, 0),
        ("42", None, 42),
        ("  42  ", None, 42),
        ("-5", None, -5),
        ("  +10  ", None, 10),
        ("invalid", None, None),
        ("invalid", 1, 1),
        ([], None, None),  # List -> default (line 72->79)
        ({}, 0, 0),  # Dict -> default
    ],
)
def test_types_to_int(
    value: object, default: int | None, expected: int | None
) -> None:
    """Test types_to_int() for ints, floats, strings, and defaults."""
    assert types_to_int(value, default) == expected


def test_types_to_int_pattern_match() -> None:
    """Test types_to_int with pattern match fallback (line 89)."""
    # String that fails direct conversion but matches pattern
    result = types_to_int("  42abc", None)
    assert result is None  # Pattern won't match with trailing chars

    # Valid int with whitespace uses pattern
    result = types_to_int("  99  ", None)
    assert result == 99
