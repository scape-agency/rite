# =============================================================================
# Test: documentation_get_file
# =============================================================================

"""
Tests for rite.reflection.documentation.documentation_get_file.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.reflection.documentation.documentation_get_file import (
    documentation_get_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_documentation_get_file() -> None:
    """Test documentation_get_file() with module."""
    # Import | Standard Library
    import json

    result = documentation_get_file(json)
    assert result is not None
    assert result.endswith(".py") or result.endswith(".so")


def test_documentation_get_file_with_function() -> None:
    """Test documentation_get_file() with function."""

    def test_func():
        pass

    result = documentation_get_file(test_func)
    # For local functions defined in test, result should be the test file
    assert result is not None


def test_documentation_get_file_builtin_type() -> None:
    """Test documentation_get_file() with built-in type."""
    result = documentation_get_file(int)
    # Built-in types may not have files
    assert result is None or isinstance(result, str)
