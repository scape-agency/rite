# =============================================================================
# Test: shell_split
# =============================================================================

"""
Tests for rite.system.shell.shell_split.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.shell.shell_split import (
    shell_split,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_shell_split() -> None:
    """Test shell_split() function."""
    # Test simple command
    result = shell_split("ls -la")
    assert result == ["ls", "-la"]

    # Test with quoted arguments
    result = shell_split("echo 'hello world'")
    assert result == ["echo", "hello world"]

    # Test with escaped quotes
    result = shell_split("ls '/tmp/file name.txt'")
    assert result == ["ls", "/tmp/file name.txt"]
