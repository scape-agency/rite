# =============================================================================
# Test: to_bool
# =============================================================================

"""
Tests for rite.conversion.to_bool.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.to_bool import to_bool

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        (True, True),
        (False, False),
        (1, True),
        (0, False),
        (1.0, True),
        (0.0, False),
        ("yes", True),
        ("YeS", True),
        ("no", False),
        ("OFF", False),
        ("", False),
        ("true", True),
        ("false", False),
    ],
)
def test_to_bool_basic_conversions(value: object, expected: bool) -> None:
    """Convert common truthy and falsy representations correctly."""
    assert to_bool(value) is expected


def test_to_bool_none_and_unknown() -> None:
    """Return None for None and unrecognised string values."""
    assert to_bool(None) is None
    assert to_bool("maybe") is None
