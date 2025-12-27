# =============================================================================
# Test: env_get
# =============================================================================

"""
Tests for rite.system.environment.env_get.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.environment.env_get import (
    env_get,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_env_get() -> None:
    """Test env_get() function."""
    import os
    # Set a test variable
    os.environ["TEST_VAR"] = "test_value"
    
    # Test get existing
    assert env_get("TEST_VAR") == "test_value"
    
    # Test get non-existing with default
    assert env_get("NON_EXISTENT", "default") == "default"
    
    # Test get non-existing without default
    assert env_get("NON_EXISTENT") is None
    
    # Cleanup
    del os.environ["TEST_VAR"]
