# =============================================================================
# Test: attributes_del_attr
# =============================================================================

"""
Tests for rite.reflection.attributes.attributes_del_attr.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.attributes.attributes_del_attr import (
    attributes_del_attr,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_attributes_del_attr() -> None:
    """Test attributes_del_attr() with various objects."""

    class TestClass:
        def __init__(self) -> None:
            self.value = 42
            self.name = "test"

    obj = TestClass()
    assert hasattr(obj, "value")
    attributes_del_attr(obj, "value")
    assert not hasattr(obj, "value")

    assert hasattr(obj, "name")
    attributes_del_attr(obj, "name")
    assert not hasattr(obj, "name")
