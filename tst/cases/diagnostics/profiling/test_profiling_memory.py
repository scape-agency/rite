# =============================================================================
# Test: profiling_memory
# =============================================================================

"""
Tests for rite.diagnostics.profiling.profiling_memory.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.profiling.profiling_memory import (
    profiling_memory,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_profiling_memory() -> None:
    """Test profiling_memory() decorator."""
    # Import | Standard Library
    import io
    import sys

    # Test basic memory profiling
    @profiling_memory(print_result=False)
    def allocate_memory() -> list:
        return [0] * 1000

    result = allocate_memory()
    assert isinstance(result, list)
    assert len(result) == 1000

    # Test with print enabled
    @profiling_memory(print_result=True)
    def allocate_with_print() -> list:
        return [1] * 100

    captured_output = io.StringIO()
    sys.stdout = captured_output

    result = allocate_with_print()

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "allocate_with_print:" in output
    assert "MB memory delta" in output

    # Test that function result is preserved
    @profiling_memory(print_result=False)
    def returns_value() -> str:
        return "test_value"

    result = returns_value()
    assert result == "test_value"

    # Test with arguments
    @profiling_memory(print_result=False)
    def func_with_args(a: int, b: str) -> str:
        return f"{a}:{b}"

    result = func_with_args(42, "test")
    assert result == "42:test"

    # Test empty function
    @profiling_memory(print_result=False)
    def empty_func() -> None:
        pass

    empty_func()  # Should not raise

    # Test function with exception (memory decorator should not interfere)
    @profiling_memory(print_result=False)
    def raises_error() -> None:
        raise ValueError("test error")

    with pytest.raises(ValueError):
        raises_error()
