# =============================================================================
# Test: documentation_get_docstring
# =============================================================================

"""
Tests for rite.reflection.documentation.documentation_get_docstring.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.documentation.documentation_get_docstring import (
    documentation_get_docstring,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_documentation_get_docstring() -> None:
    """Test documentation_get_docstring() with function."""

    def test_func():
        """This is a test docstring."""
        pass

    result = documentation_get_docstring(test_func)
    assert result == "This is a test docstring."


def test_documentation_get_docstring_multiline() -> None:
    """Test documentation_get_docstring() with multiline docstring."""

    def test_func():
        """First line.

        Second paragraph.
        """
        pass

    result = documentation_get_docstring(test_func)
    assert "First line." in result
    assert "Second paragraph." in result


def test_documentation_get_docstring_no_docstring() -> None:
    """Test documentation_get_docstring() with no docstring."""

    def test_func():
        pass

    result = documentation_get_docstring(test_func)
    assert result is None


def test_documentation_get_docstring_builtin() -> None:
    """Test documentation_get_docstring() with built-in."""
    result = documentation_get_docstring(len)
    assert result is not None
    assert isinstance(result, str)
