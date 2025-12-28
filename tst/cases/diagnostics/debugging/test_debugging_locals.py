# =============================================================================
# Test: debugging_locals
# =============================================================================

"""
Tests for rite.diagnostics.debugging.debugging_locals.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.debugging.debugging_locals import (
    debugging_locals,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_debugging_locals_captures_variables(capsys) -> None:
    """Test debugging_locals captures local variables."""

    def test_func():
        x = 42
        y = "hello"
        result = debugging_locals()
        assert "x" in result
        assert "y" in result
        assert result["x"] == 42
        assert result["y"] == "hello"
        return result

    result = test_func()
    captured = capsys.readouterr()
    assert "LOCAL VARIABLES" in captured.out


def test_debugging_locals_excludes_private(capsys) -> None:
    """Test debugging_locals excludes private by default."""

    def test_func():
        x = 1
        _private = 2
        result = debugging_locals(show_private=False)
        assert "x" in result
        assert "_private" not in result
        return result

    result = test_func()
    assert result["x"] == 1


def test_debugging_locals_includes_private(capsys) -> None:
    """Test debugging_locals includes private when requested."""

    def test_func():
        x = 1
        _private = 2
        result = debugging_locals(show_private=True)
        assert "x" in result
        assert "_private" in result
        return result

    result = test_func()
    assert result["x"] == 1
    assert result["_private"] == 2
