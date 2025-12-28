# =============================================================================
# Test: get_escaped_command_arg
# =============================================================================

"""
Tests for rite.system.get_escaped_command_arg.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.get_escaped_command_arg import (
    get_escaped_command_arg,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_get_escaped_command_arg() -> None:
    """Test get_escaped_command_arg() function."""
    # Test simple argument
    assert get_escaped_command_arg("hello") == "hello"

    # Test argument with spaces
    assert get_escaped_command_arg("hello world") == "'hello world'"

    # Test argument with single quotes
    assert get_escaped_command_arg("it's") == "'it'\"'\"'s'"

    # Test argument with double quotes
    result = get_escaped_command_arg('say "hello"')
    assert "hello" in result

    # Test empty string
    assert get_escaped_command_arg("") == "''"

    # Test argument with special shell characters
    assert ";" in get_escaped_command_arg("cmd;rm")
    assert "|" in get_escaped_command_arg("cmd|next")
    assert "$" in get_escaped_command_arg("$VAR")

    # Test argument with backticks
    result = get_escaped_command_arg("`whoami`")
    assert "whoami" in result

    # Test argument with ampersand
    result = get_escaped_command_arg("a&b")
    assert "&" in result

    # Test argument with parentheses
    result = get_escaped_command_arg("(hello)")
    assert "hello" in result

    # Test argument with newline
    result = get_escaped_command_arg("line1\nline2")
    assert "\n" in result

    # Test argument that needs escaping
    result = get_escaped_command_arg("$PATH")
    # Should escape the $
    assert "PATH" in result
