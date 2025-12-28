# =============================================================================
# Test: signature_get_return_annotation
# =============================================================================

"""
Tests for rite.reflection.signature.signature_get_return_annotation.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import inspect

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.signature.signature_get_return_annotation import (
    signature_get_return_annotation,
)

# =============================================================================
# Test Functions
# =============================================================================

# =============================================================================
# Test Functions
# =============================================================================


class TestSignatureGetReturnAnnotation:
    """Tests for signature_get_return_annotation function."""

    def test_with_return_annotation(self) -> None:
        """Test with function that has return annotation."""
        def func(a: int) -> str:
            return str(a)
        
        result = signature_get_return_annotation(func)
        # With __future__ import, annotation is a string
        assert "str" in str(result)

    def test_with_int_return(self) -> None:
        """Test with int return annotation."""
        def func(a: str) -> int:
            return len(a)
        
        result = signature_get_return_annotation(func)
        assert "int" in str(result)

    def test_with_none_return(self) -> None:
        """Test with None return annotation."""
        def func(a: int) -> None:
            print(a)
        
        result = signature_get_return_annotation(func)
        # With __future__ import, it's a string
        assert "None" in str(result)

    def test_without_return_annotation(self) -> None:
        """Test with function without return annotation."""
        def func(a: int):
            return a
        
        result = signature_get_return_annotation(func)
        # Should return Signature.empty when no annotation
        assert result == inspect.Signature.empty

    def test_with_complex_annotation(self) -> None:
        """Test with complex return type annotation."""
        def func(a: int) -> list[str]:
            return [str(a)]
        
        result = signature_get_return_annotation(func)
        # With __future__ import, it's a string
        assert "list" in str(result)

    def test_with_union_return(self) -> None:
        """Test with union return annotation."""
        def func(a: int) -> str | int:
            return a if isinstance(a, int) else str(a)
        
        result = signature_get_return_annotation(func)
        # With __future__ import, it's a string
        assert "|" in str(result) or "Union" in str(result)

    def test_with_custom_class_return(self) -> None:
        """Test with custom class return annotation."""
        class MyClass:
            pass
        
        def func() -> MyClass:
            return MyClass()
        
        result = signature_get_return_annotation(func)
        # With __future__ import, it's a string
        assert "MyClass" in str(result)

    def test_with_dict_return(self) -> None:
        """Test with dict return annotation."""
        def func(a: int) -> dict[str, int]:
            return {"value": a}
        
        result = signature_get_return_annotation(func)
        # With __future__ import, it's a string
        assert "dict" in str(result)
