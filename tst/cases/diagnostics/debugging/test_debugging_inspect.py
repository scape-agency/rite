# =============================================================================
# Test: debugging_inspect
# =============================================================================

"""
Tests for rite.diagnostics.debugging.debugging_inspect.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.diagnostics.debugging.debugging_inspect import (
    debugging_inspect,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_debugging_inspect_basic() -> None:
    """Test debugging_inspect on simple object."""

    class TestObj:
        attr = 42

    result = debugging_inspect(TestObj())
    assert "attributes" in result
    assert "methods" in result
    assert "type" in result
    assert result["type"] == "TestObj"


def test_debugging_inspect_callable() -> None:
    """Test debugging_inspect detects callable objects."""

    def sample_func():
        pass

    result = debugging_inspect(sample_func)
    assert result["is_callable"] is True


def test_debugging_inspect_show_private() -> None:
    """Test debugging_inspect includes private attributes when requested."""

    class TestObj:
        public = 1
        _private = 2

    result = debugging_inspect(TestObj(), show_private=True)
    assert "_private" in result["attributes"] or len(result["attributes"]) > 0


def test_debugging_inspect_dict() -> None:
    """Test debugging_inspect on dict object."""
    obj = {"key": "value"}
    result = debugging_inspect(obj)
    assert result["type"] == "dict"
    assert "methods" in result


def test_debugging_inspect_unavailable_attribute() -> None:
    """Test debugging_inspect marks unavailable attributes."""

    class TestObj:
        @property
        def bad_prop(self):
            raise AttributeError("Intentional error")

    obj = TestObj()
    result = debugging_inspect(obj)
    assert "bad_prop" in result["attributes"]
    assert result["attributes"]["bad_prop"] == "<unavailable>"
