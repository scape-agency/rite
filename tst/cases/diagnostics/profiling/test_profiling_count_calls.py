# =============================================================================
# Test: profiling_count_calls
# =============================================================================

"""
Tests for rite.diagnostics.profiling.profiling_count_calls.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.profiling.profiling_count_calls import (
    profiling_count_calls,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_profiling_count_calls() -> None:
    """Test profiling_count_calls() decorator."""
    # Import | Standard Library
    import io
    import sys

    # Test basic call counting
    @profiling_count_calls()
    def func1() -> None:
        pass

    assert func1.call_count == 0
    func1()
    assert func1.call_count == 1
    func1()
    assert func1.call_count == 2

    # Test with arguments
    @profiling_count_calls()
    def func2(a: int, b: str) -> str:
        return f"{a}:{b}"

    func2(1, "test")
    assert func2.call_count == 1
    result = func2(2, "test2")
    assert func2.call_count == 2
    assert result == "2:test2"

    # Test print_every functionality
    @profiling_count_calls(print_every=2)
    def func3() -> None:
        pass

    captured_output = io.StringIO()
    sys.stdout = captured_output

    func3()  # count=1, no print
    func3()  # count=2, print

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "func3 called 2 times" in output
    assert func3.call_count == 2

    # Test multiple decorators
    @profiling_count_calls()
    def func4() -> int:
        return 42

    @profiling_count_calls()
    def func5() -> int:
        return 99

    func4()
    func4()
    func5()

    assert func4.call_count == 2
    assert func5.call_count == 1

    # Test return value is preserved
    @profiling_count_calls()
    def returns_tuple() -> tuple[int, str]:
        return (123, "result")

    result = returns_tuple()
    assert result == (123, "result")
    assert returns_tuple.call_count == 1
