# =============================================================================
# Test: platform_is_windows
# =============================================================================

"""
Tests for rite.system.platform.platform_is_windows.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.platform.platform_is_windows import (
    platform_is_windows,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_platform_is_windows() -> None:
    """Test platform_is_windows() function."""
    # Test returns bool
    result = platform_is_windows()
    assert isinstance(result, bool)
    # On macOS, should be False
    assert result is False
