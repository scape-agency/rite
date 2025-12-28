# =============================================================================
# Test: debugging_trace
# =============================================================================

"""
Tests for rite.diagnostics.debugging.debugging_trace.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.debugging.debugging_trace import (
    debugging_trace,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_debugging_trace() -> None:
    """Test debugging_trace() decorator."""
    # Import | Standard Library
    import io
    import sys

    # Test basic tracing
    @debugging_trace()
    def add(a: int, b: int) -> int:
        return a + b

    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = add(2, 3)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert result == 5
    assert "→ add(2, 3)" in output
    assert "← add = 5" in output

    # Test with kwargs
    @debugging_trace()
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = greet("Alice", greeting="Hi")
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert result == "Hi, Alice!"
    assert "→ greet" in output
    assert "greeting=" in output

    # Test without showing return
    @debugging_trace(show_return=False)
    def process() -> None:
        pass

    captured_output = io.StringIO()
    sys.stdout = captured_output
    process()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "→ process()" in output
    assert "← process" in output

    # Test without showing args
    @debugging_trace(show_args=False)
    def multiply(x: int, y: int) -> int:
        return x * y

    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = multiply(4, 5)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert result == 20
    assert "→ multiply()" in output
    assert "← multiply = 20" in output

    # Test without showing args or return
    @debugging_trace(show_args=False, show_return=False)
    def silent() -> str:
        return "hidden"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = silent()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert result == "hidden"
    assert "→ silent()" in output
    assert "← silent" in output
