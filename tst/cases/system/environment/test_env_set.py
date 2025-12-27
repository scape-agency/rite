# =============================================================================
# Test: env_set
# =============================================================================

"""
Tests for rite.system.environment.env_set.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.environment.env_set import (
    env_set,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_env_set() -> None:
    """Test env_set() function."""
    import os
    # Test set
    env_set("TEST_VAR", "test_value")
    assert os.environ.get("TEST_VAR") == "test_value"
    
    # Test overwrite
    env_set("TEST_VAR", "new_value")
    assert os.environ.get("TEST_VAR") == "new_value"
    
    # Cleanup
    del os.environ["TEST_VAR"]
