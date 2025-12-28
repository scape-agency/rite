# =============================================================================
# Test: signature_get_signature
# =============================================================================

"""
Tests for rite.reflection.signature.signature_get_signature.
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
from rite.reflection.signature.signature_get_signature import (
    signature_get_signature,
)

# =============================================================================
# Test Functions
# =============================================================================

# =============================================================================
# Test Functions
# =============================================================================


class TestSignatureGetSignature:
    """Tests for signature_get_signature function."""

    def test_returns_signature(self) -> None:
        """Test that function returns Signature object."""

        def func(a: int, b: str = "default") -> str:
            return f"{a}{b}"

        result = signature_get_signature(func)
        assert isinstance(result, inspect.Signature)

    def test_signature_parameters(self) -> None:
        """Test that signature contains parameters."""

        def func(a: int, b: str = "default") -> str:
            return f"{a}{b}"

        sig = signature_get_signature(func)
        assert len(sig.parameters) == 2
        assert "a" in sig.parameters
        assert "b" in sig.parameters

    def test_signature_return_annotation(self) -> None:
        """Test that signature contains return annotation."""

        def func(a: int) -> str:
            return str(a)

        sig = signature_get_signature(func)
        # With __future__ import, annotation is a string
        assert "str" in str(sig.return_annotation)

    def test_signature_string_representation(self) -> None:
        """Test string representation of signature."""

        def func(a: int, b: str = "default") -> str:
            return f"{a}{b}"

        sig = signature_get_signature(func)
        sig_str = str(sig)
        # Should contain parameter info
        assert "a" in sig_str
        assert "int" in sig_str

    def test_signature_with_no_params(self) -> None:
        """Test signature with no parameters."""

        def func() -> int:
            return 42

        sig = signature_get_signature(func)
        assert len(sig.parameters) == 0
        # Annotation is a string with __future__ import
        assert "int" in str(sig.return_annotation)

    def test_signature_with_complex_types(self) -> None:
        """Test signature with complex type annotations."""

        def func(data: list[dict[str, int]]) -> tuple[str, int]:
            pass

        sig = signature_get_signature(func)
        assert "data" in sig.parameters
        # With __future__ import, annotation is a string
        assert "list" in str(sig.parameters["data"].annotation)

    def test_signature_with_args_kwargs(self) -> None:
        """Test signature with *args and **kwargs."""

        def func(a: int, *args, **kwargs) -> None:
            pass

        sig = signature_get_signature(func)
        assert "a" in sig.parameters
        assert "args" in sig.parameters
        assert "kwargs" in sig.parameters

    def test_signature_with_defaults(self) -> None:
        """Test that defaults are captured in signature."""

        def func(a: int = 10, b: str = "hello") -> str:
            return f"{a}{b}"

        sig = signature_get_signature(func)
        assert sig.parameters["a"].default == 10
        assert sig.parameters["b"].default == "hello"

    def test_signature_with_class(self) -> None:
        """Test signature of a class constructor."""

        class MyClass:
            def __init__(self, x: int, y: str = "default"):
                self.x = x
                self.y = y

        sig = signature_get_signature(MyClass)
        # Should include parameters (except self)
        assert "x" in sig.parameters or "self" in sig.parameters
