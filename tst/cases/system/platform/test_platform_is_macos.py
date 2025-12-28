# =============================================================================
# Test: platform_is_macos
# =============================================================================

"""
Tests for rite.system.platform.platform_is_macos.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import sys

# Import | Local Modules
from rite.system.platform.platform_is_macos import (
    platform_is_macos,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_platform_is_macos() -> None:
    """Test platform_is_macos() function."""
    # Test returns bool
    result = platform_is_macos()
    assert isinstance(result, bool)
    # Result should match sys.platform check
    expected = sys.platform == "darwin"
    assert result is expected
