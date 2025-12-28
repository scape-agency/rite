# =============================================================================
# Test: platform_is_linux
# =============================================================================

"""
Tests for rite.system.platform.platform_is_linux.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import sys

# Import | Local Modules
from rite.system.platform.platform_is_linux import (
    platform_is_linux,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_platform_is_linux() -> None:
    """Test platform_is_linux() function."""
    # Test returns bool
    result = platform_is_linux()
    assert isinstance(result, bool)
    # Result should match sys.platform check
    expected = sys.platform.startswith("linux")
    assert result is expected
