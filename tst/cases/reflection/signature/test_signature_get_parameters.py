# =============================================================================
# Test: signature_get_parameters
# =============================================================================

"""
Tests for rite.reflection.signature.signature_get_parameters.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import inspect

# Import | Local Modules
from rite.reflection.signature.signature_get_parameters import (
    signature_get_parameters,
)

# =============================================================================
# Test Functions
# =============================================================================

# =============================================================================
# Test Functions
# =============================================================================


class TestSignatureGetParameters:
    """Tests for signature_get_parameters function."""

    def test_returns_dict(self) -> None:
        """Test that function returns a dictionary."""

        def func(a: int, b: str = "default") -> str:
            return f"{a}{b}"

        result = signature_get_parameters(func)
        assert isinstance(result, dict)

    def test_contains_all_parameters(self) -> None:
        """Test that all parameters are in the dictionary."""

        def func(a: int, b: str = "default") -> str:
            return f"{a}{b}"

        result = signature_get_parameters(func)
        assert "a" in result
        assert "b" in result

    def test_parameter_objects(self) -> None:
        """Test that values are Parameter objects."""

        def func(a: int, b: str = "default") -> str:
            return f"{a}{b}"

        result = signature_get_parameters(func)
        for param in result.values():
            assert isinstance(param, inspect.Parameter)

    def test_no_parameters_function(self) -> None:
        """Test with function that has no parameters."""

        def no_params():
            return 42

        result = signature_get_parameters(no_params)
        assert isinstance(result, dict)
        assert len(result) == 0

    def test_with_defaults(self) -> None:
        """Test with parameters that have defaults."""

        def func(a: int, b: str = "default", c: float = 3.14) -> str:
            return f"{a}{b}{c}"

        result = signature_get_parameters(func)
        assert result["b"].default == "default"
        assert result["c"].default == 3.14

    def test_with_annotations(self) -> None:
        """Test that annotations are preserved."""

        def func(a: int, b: str = "default") -> str:
            return f"{a}{b}"

        result = signature_get_parameters(func)
        # Annotations are strings due to __future__ import
        assert "int" in str(result["a"].annotation)
        assert "str" in str(result["b"].annotation)

    def test_with_args_kwargs(self) -> None:
        """Test with *args and **kwargs."""

        def func(a: int, *args, **kwargs):
            pass

        result = signature_get_parameters(func)
        assert "a" in result
        assert "args" in result
        assert "kwargs" in result
        assert result["args"].kind == inspect.Parameter.VAR_POSITIONAL
        assert result["kwargs"].kind == inspect.Parameter.VAR_KEYWORD

    def test_parameter_names_as_keys(self) -> None:
        """Test that parameter names are the dictionary keys."""

        def func(param_one: int, param_two: str) -> str:
            return f"{param_one}{param_two}"

        result = signature_get_parameters(func)
        assert list(result.keys()) == ["param_one", "param_two"]
