# =============================================================================
# Test: env_delete
# =============================================================================

"""
Tests for rite.system.environment.env_delete.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.environment.env_delete import (
    env_delete,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_env_delete() -> None:
    """Test env_delete() function."""
    # Import | Standard Library
    import os

    # Set a test variable
    os.environ["TEST_VAR"] = "test_value"
    assert "TEST_VAR" in os.environ

    # Test delete
    env_delete("TEST_VAR")
    assert "TEST_VAR" not in os.environ

    # Test delete non-existent (should not raise)
    env_delete("NON_EXISTENT")
