# =============================================================================
# Test: profiling_timer
# =============================================================================

"""
Tests for rite.diagnostics.profiling.profiling_timer.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.profiling.profiling_timer import (
    profiling_timer,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_profiling_timer() -> None:
    """Test profiling_timer() decorator."""
    # Import | Standard Library
    import io
    import sys
    import time

    # Test basic timing
    @profiling_timer(print_result=False)
    def quick_func() -> None:
        time.sleep(0.01)

    quick_func()  # Should complete without error

    # Test with print enabled
    @profiling_timer(print_result=True)
    def timed_func() -> None:
        time.sleep(0.01)

    captured_output = io.StringIO()
    sys.stdout = captured_output

    timed_func()

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "timed_func:" in output
    assert "seconds" in output

    # Test with custom name
    @profiling_timer(name="CustomOperation", print_result=True)
    def func_with_custom_name() -> None:
        pass

    captured_output = io.StringIO()
    sys.stdout = captured_output

    func_with_custom_name()

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "CustomOperation:" in output

    # Test return value is preserved
    @profiling_timer(print_result=False)
    def returns_value() -> str:
        return "test_result"

    result = returns_value()
    assert result == "test_result"

    # Test with arguments
    @profiling_timer(print_result=False)
    def func_with_args(a: int, b: str) -> str:
        return f"{a}:{b}"

    result = func_with_args(10, "test")
    assert result == "10:test"

    # Test exception handling (should still print time)
    @profiling_timer(print_result=True)
    def raises_error() -> None:
        raise ValueError("test error")

    captured_output = io.StringIO()
    sys.stdout = captured_output

    with pytest.raises(ValueError):
        raises_error()

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    # Should have printed timing even though exception was raised
    assert "raises_error:" in output

    # Test timing accuracy (rough check)
    @profiling_timer(print_result=False)
    def sleepy() -> None:
        time.sleep(0.05)

    start = time.perf_counter()
    sleepy()
    elapsed = time.perf_counter() - start
    assert elapsed >= 0.04  # Allow small variance
