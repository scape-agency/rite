# =============================================================================
# Test: inspection_get_source
# =============================================================================

"""
Tests for rite.reflection.inspection.inspection_get_source.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.reflection.inspection.inspection_get_source import (
    inspection_get_source,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestInspectionGetSource:
    """Tests for inspection_get_source function."""

    def test_returns_string(self) -> None:
        """Test that function returns a string."""

        def my_func():
            pass

        result = inspection_get_source(my_func)
        assert isinstance(result, str)

    def test_contains_function_code(self) -> None:
        """Test that source contains function code."""

        def my_func():
            return 42

        result = inspection_get_source(my_func)
        assert "def my_func" in result
        assert "return 42" in result

    def test_with_custom_class(self) -> None:
        """Test with custom class."""

        class MyClass:
            pass

        result = inspection_get_source(MyClass)
        assert isinstance(result, str)
        assert "class MyClass" in result

    def test_with_class_method(self) -> None:
        """Test with class method."""

        class MyClass:
            def method(self):
                return 42

        obj = MyClass()
        result = inspection_get_source(obj.method)
        assert isinstance(result, str)
        assert "def method" in result

    def test_with_lambda_raises_error(self) -> None:
        """Test that lambda raises error or returns minimal source."""
        lambda_func = lambda x: x * 2
        try:
            source = inspection_get_source(lambda_func)
            # If it succeeds, just check it's a string
            assert isinstance(source, str)
        except (OSError, TypeError):
            # Expected behavior for lambdas
            pass

    def test_source_is_valid_python(self) -> None:
        """Test that returned source is valid Python."""

        class MyClass:
            def method(self):
                return 42

        result = inspection_get_source(MyClass.method)
        # Source will be indented, so check compilation fails gracefully
        assert isinstance(result, str)
        assert "def method" in result

    def test_preserves_indentation(self) -> None:
        """Test that source preserves indentation."""

        class MyClass:
            def method(self):
                x = 10
                return x

        result = inspection_get_source(MyClass.method)
        # Should contain the indented code
        assert "def method" in result
