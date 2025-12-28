# =============================================================================
# Test: shell_join
# =============================================================================

"""
Tests for rite.system.shell.shell_join.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.shell.shell_join import (
    shell_join,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_shell_join() -> None:
    """Test shell_join() function."""
    # Test simple command
    result = shell_join(["ls", "-la"])
    assert result == "ls -la"

    # Test with arguments containing spaces
    result = shell_join(["echo", "hello world"])
    assert result == "echo 'hello world'"

    # Test single argument
    result = shell_join(["ls"])
    assert result == "ls"
