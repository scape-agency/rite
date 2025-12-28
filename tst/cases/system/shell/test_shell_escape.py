# =============================================================================
# Test: shell_escape
# =============================================================================

"""
Tests for rite.system.shell.shell_escape.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.shell.shell_escape import (
    shell_escape,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_shell_escape() -> None:
    """Test shell_escape() function."""
    # Test with spaces
    result = shell_escape("file name.txt")
    assert result == "'file name.txt'"

    # Test simple string (no escaping needed)
    result = shell_escape("simple")
    assert result == "simple"

    # Test with special characters
    result = shell_escape("test$var")
    assert "$" not in result or "'" in result
