# =============================================================================
# Test: platform_python_version
# =============================================================================

"""
Tests for rite.system.platform.platform_python_version.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.platform.platform_python_version import (
    platform_python_version,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_platform_python_version() -> None:
    """Test platform_python_version() function."""
    # Test returns string
    result = platform_python_version()
    assert isinstance(result, str)
    assert len(result) > 0
    # Should contain dots and digits
    assert "." in result
    parts = result.split(".")
    assert len(parts) >= 2
    # Should be Python 3.x
    assert parts[0] == "3"
