# =============================================================================
# Test: is_protected_type
# =============================================================================

"""
Tests for rite.conversion.is_protected_type.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import datetime
from decimal import Decimal

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.is_protected_type import is_protected_type

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        (None, True),
        (0, True),
        (1.5, True),
        (Decimal("2.5"), True),
        (datetime.datetime.now(), True),
        (datetime.date.today(), True),
        (datetime.time(12, 0), True),
        ("not protected", False),
        ([1, 2, 3], False),
    ],
)
def test_is_protected_type(value: object, expected: bool) -> None:
    """Return True only for configured protected scalar types."""
    assert is_protected_type(value) is expected
