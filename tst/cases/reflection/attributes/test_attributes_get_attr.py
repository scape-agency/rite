# =============================================================================
# Test: attributes_get_attr
# =============================================================================

"""
Tests for rite.reflection.attributes.attributes_get_attr.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.attributes.attributes_get_attr import (
    attributes_get_attr,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_attributes_get_attr() -> None:
    """Test attributes_get_attr() with various objects."""

    class TestClass:
        def __init__(self) -> None:
            self.value = 42
            self.name = "test"

    obj = TestClass()
    assert attributes_get_attr(obj, "value") == 42
    assert attributes_get_attr(obj, "name") == "test"
    assert attributes_get_attr(obj, "missing") is None
    assert attributes_get_attr(obj, "missing", "default") == "default"
    assert attributes_get_attr("hello", "upper") is not None
