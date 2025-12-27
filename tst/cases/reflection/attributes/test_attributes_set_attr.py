# =============================================================================
# Test: attributes_set_attr
# =============================================================================

"""
Tests for rite.reflection.attributes.attributes_set_attr.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.attributes.attributes_set_attr import (
    attributes_set_attr,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_attributes_set_attr() -> None:
    """Test attributes_set_attr() with various objects."""

    class TestClass:
        pass

    obj = TestClass()
    attributes_set_attr(obj, "value", 42)
    assert obj.value == 42

    attributes_set_attr(obj, "name", "test")
    assert obj.name == "test"

    attributes_set_attr(obj, "value", 100)
    assert obj.value == 100
