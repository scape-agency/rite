# =============================================================================
# Test: errors_format_traceback
# =============================================================================

"""
Tests for rite.diagnostics.errors.errors_format_traceback.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.errors.errors_format_traceback import (
    errors_format_traceback,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_errors_format_traceback_basic() -> None:
    """Test errors_format_traceback formats exception."""
    try:
        raise ValueError("test error")
    except ValueError as e:
        result = errors_format_traceback(e)
        assert "ValueError" in result
        assert "test error" in result


def test_errors_format_traceback_with_locals() -> None:
    """Test errors_format_traceback with local variables."""
    try:
        x = 42
        y = "test"
        raise RuntimeError("error")
    except RuntimeError as e:
        result = errors_format_traceback(e, include_locals=True)
        assert "RuntimeError" in result
        assert "Local variables" in result


def test_errors_format_traceback_without_locals() -> None:
    """Test errors_format_traceback without local variables."""
    try:
        raise TypeError("type error")
    except TypeError as e:
        result = errors_format_traceback(e, include_locals=False)
        assert "TypeError" in result
        # Should not include locals section
        assert "Local variables" not in result


def test_errors_format_traceback_unrepresentable_locals() -> None:
    """Test errors_format_traceback with unrepresentable local variables."""

    class BadRepr:
        def __repr__(self):
            raise ValueError("Bad repr")

    try:
        bad_obj = BadRepr()
        raise RuntimeError("error with bad repr")
    except RuntimeError as e:
        result = errors_format_traceback(e, include_locals=True)
        assert "RuntimeError" in result
        # Should handle the unrepresentable object gracefully
        assert "<unrepresentable>" in result or "bad_obj" in result


def test_errors_format_traceback_nested() -> None:
    """Test errors_format_traceback with nested exceptions."""
    try:
        try:
            raise ValueError("inner")
        except ValueError as inner_e:
            raise KeyError("outer") from inner_e
    except KeyError as e:
        result = errors_format_traceback(e)
        assert "KeyError" in result
