# =============================================================================
# Test: env_list
# =============================================================================

"""
Tests for rite.system.environment.env_list.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.environment.env_list import (
    env_list,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_env_list() -> None:
    """Test env_list() function."""
    # Test returns dict
    result = env_list()
    assert isinstance(result, dict)

    # Test contains standard env vars
    assert len(result) > 0
    assert "PATH" in result or "Path" in result  # Cross-platform
