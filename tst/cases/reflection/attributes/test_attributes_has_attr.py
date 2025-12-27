# =============================================================================
# Test: attributes_has_attr
# =============================================================================

"""
Tests for rite.reflection.attributes.attributes_has_attr.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.attributes.attributes_has_attr import (
    attributes_has_attr,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_attributes_has_attr() -> None:
    """Test attributes_has_attr() with various objects."""

    class TestClass:
        def __init__(self) -> None:
            self.value = 42

    obj = TestClass()
    assert attributes_has_attr(obj, "value") is True
    assert attributes_has_attr(obj, "missing") is False
    assert attributes_has_attr("hello", "upper") is True
    assert attributes_has_attr("hello", "missing_method") is False
