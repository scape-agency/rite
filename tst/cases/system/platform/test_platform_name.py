# =============================================================================
# Test: platform_name
# =============================================================================

"""
Tests for rite.system.platform.platform_name.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.platform.platform_name import (
    platform_name,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_platform_name() -> None:
    """Test platform_name() function."""
    # Test returns string
    result = platform_name()
    assert isinstance(result, str)
    assert len(result) > 0
    # On macOS, should be Darwin
    assert result == "Darwin"
