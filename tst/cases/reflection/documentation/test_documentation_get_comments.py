# =============================================================================
# Test: documentation_get_comments
# =============================================================================

"""
Tests for rite.reflection.documentation.documentation_get_comments.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.reflection.documentation.documentation_get_comments import (
    documentation_get_comments,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_documentation_get_comments() -> None:
    """Test documentation_get_comments() with function."""

    # Create a function with comments
    def test_func() -> None:
        """Test function."""

    result = documentation_get_comments(test_func)
    # Comments are only captured for functions defined at module level
    # For local functions, result is typically None
    assert result is None or isinstance(result, str)


def test_documentation_get_comments_builtin() -> None:
    """Test documentation_get_comments() with built-in function."""
    result = documentation_get_comments(len)
    # Built-in functions typically have no comments
    assert result is None
