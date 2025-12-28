# =============================================================================
# Test: debugging_dump
# =============================================================================

"""
Tests for rite.diagnostics.debugging.debugging_dump.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.debugging.debugging_dump import (
    debugging_dump,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_debugging_dump() -> None:
    """Test debugging_dump() function."""
    # Import | Standard Library
    import io
    import sys

    # Test with positional arguments
    captured_output = io.StringIO()
    sys.stdout = captured_output
    debugging_dump(42, "hello")
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "ARG 0: 42" in output
    assert "ARG 1: 'hello'" in output

    # Test with keyword arguments
    captured_output = io.StringIO()
    sys.stdout = captured_output
    debugging_dump(status="active", count=5)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "status:" in output
    assert "active" in output
    assert "count:" in output
    assert "5" in output

    # Test with dict
    captured_output = io.StringIO()
    sys.stdout = captured_output
    debugging_dump(data={"key": "value"})
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "data:" in output

    # Test with list
    captured_output = io.StringIO()
    sys.stdout = captured_output
    debugging_dump([1, 2, 3, 4, 5])
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "ARG 0:" in output

    # Test with empty call
    captured_output = io.StringIO()
    sys.stdout = captured_output
    debugging_dump()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == ""

    # Test with mixed args and kwargs
    captured_output = io.StringIO()
    sys.stdout = captured_output
    debugging_dump(1, 2, x=3, y=4)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "ARG 0: 1" in output
    assert "ARG 1: 2" in output
