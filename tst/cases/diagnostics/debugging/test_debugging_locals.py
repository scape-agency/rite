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
        var_x = 42  # pylint: disable=unused-variable
        var_y = "hello"  # pylint: disable=unused-variable
        result = debugging_locals()
        assert "var_x" in result
        assert "var_y" in result
        assert result["var_x"] == 42
        assert result["var_y"] == "hello"
        return result

    test_result = test_func()
    assert test_result is not None
    captured = capsys.readouterr()
    assert "LOCAL VARIABLES" in captured.out


def test_debugging_locals_excludes_private(capsys) -> None:
    """Test debugging_locals excludes private by default."""

    def test_func():
        var_x = 1  # pylint: disable=unused-variable
        _private = 2  # pylint: disable=unused-variable
        result = debugging_locals(show_private=False)
        assert "var_x" in result
        assert "_private" not in result
        return result

    test_result = test_func()
    assert test_result["var_x"] == 1


def test_debugging_locals_includes_private(capsys) -> None:
    """Test debugging_locals includes private when requested."""

    def test_func():
        var_x = 1  # pylint: disable=unused-variable
        _private = 2  # pylint: disable=unused-variable
        result = debugging_locals(show_private=True)
        assert "var_x" in result
        assert "_private" in result
        return result

    test_result = test_func()
    assert test_result["var_x"] == 1
    assert test_result["_private"] == 2


def test_debugging_locals_frame_none(capsys, monkeypatch) -> None:
    """Test debugging_locals when currentframe returns None (line 62)."""
    # Import | Standard Library
    import inspect  # pylint: disable=import-outside-toplevel

    # Monkeypatch to return None for currentframe
    monkeypatch.setattr(inspect, "currentframe", lambda: None)

    result = debugging_locals()
    assert result == {}


def test_debugging_locals_caller_frame_none(capsys, monkeypatch) -> None:
    """Test debugging_locals when f_back is None (line 67)."""
    # Import | Standard Library
    import inspect  # pylint: disable=import-outside-toplevel

    class FakeFrame:
        f_back = None
        f_locals = {}

    def fake_currentframe():
        return FakeFrame()

    monkeypatch.setattr(inspect, "currentframe", fake_currentframe)

    result = debugging_locals()
    assert result == {}
