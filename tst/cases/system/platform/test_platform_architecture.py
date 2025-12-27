# =============================================================================
# Test: platform_architecture
# =============================================================================

"""
Tests for rite.system.platform.platform_architecture.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.platform.platform_architecture import (
    platform_architecture,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_platform_architecture() -> None:
    """Test platform_architecture() function."""
    # Test returns string
    result = platform_architecture()
    assert isinstance(result, str)
    assert len(result) > 0
    # Common architectures
    assert result in ["x86_64", "arm64", "aarch64", "i386", "AMD64"]
