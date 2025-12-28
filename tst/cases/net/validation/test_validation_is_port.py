# =============================================================================
# Test: validation_is_port
# =============================================================================

"""
Tests for rite.net.validation.validation_is_port.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.validation.validation_is_port import (
    validation_is_port,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "port,expected",
    [
        (80, True),
        (443, True),
        (8080, True),
        (65535, True),
        (1, True),
        (0, False),
        (65536, False),
        (-1, False),
        (70000, False),
    ],
)
def test_validation_is_port(port: int, expected: bool) -> None:
    """Test validation_is_port() with various port numbers.

    Args:
        port: Port number to validate.
        expected: Whether port is valid.
    """
    result = validation_is_port(port)
    assert result == expected
