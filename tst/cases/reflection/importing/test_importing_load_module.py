# =============================================================================
# Test: importing_load_module
# =============================================================================

"""
Tests for rite.reflection.importing.importing_load_module.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.importing.importing_load_module import (
    importing_load_module,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_importing_load_module_valid_modules() -> None:
    """Test importing_load_module() with valid module names."""

    json_module = importing_load_module("json")
    assert json_module.__name__ == "json"
    assert hasattr(json_module, "dumps")

    os_path_module = importing_load_module("os.path")
    # On POSIX this is typically ``posixpath`` but we only
    # care that a module object is returned.
    assert hasattr(os_path_module, "join")


def test_importing_load_module_missing_module() -> None:
    """Test importing_load_module() with a missing module name."""

    with pytest.raises(ModuleNotFoundError):
        importing_load_module("this_module_should_not_exist_123")
