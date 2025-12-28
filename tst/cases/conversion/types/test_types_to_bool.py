# =============================================================================
# Test: types_to_bool
# =============================================================================

"""
Tests for rite.conversion.types.types_to_bool.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_bool import (
    types_to_bool,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, default, expected",
    [
        (None, None, None),
        (None, False, False),
        (True, None, True),
        (False, None, False),
        (1, None, True),
        (0, None, False),
        (2.5, None, True),
        (0.0, None, False),
        ("yes", None, True),
        ("YES", None, True),
        (" no ", None, False),
        ("Off", None, False),
        ("true", None, True),
        ("false", None, False),
        ("invalid", None, None),
        ("invalid", True, True),
        ("", False, False),  # Empty string -> default
        ("random", False, False),  # Unrecognized -> default
        (-1, None, True),  # Negative number is truthy
        ([], None, None),  # List -> not str, falls to default (branch 83->92)
        ({}, False, False),  # Dict -> not str, falls to default
    ],
)
def test_types_to_bool(
    value: object, default: bool | None, expected: bool | None
) -> None:
    """Test types_to_bool() for common truthy/falsy and default cases."""
    assert types_to_bool(value, default) is expected
