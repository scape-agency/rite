# =============================================================================
# Test: importing_load_function
# =============================================================================

"""
Tests for rite.reflection.importing.importing_load_function.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.importing.importing_load_function import (
    importing_load_function,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_importing_load_function_valid_paths() -> None:
    """Test importing_load_function() with valid function paths."""

    dumps = importing_load_function("json.dumps")
    assert dumps({"key": "value"}) == '{"key": "value"}'

    join = importing_load_function("os.path.join")
    # Behaviour should match the real os.path.join.
    # Import | Standard Library
    from os import path as os_path  # type: ignore

    assert join("a", "b") == os_path.join("a", "b")


def test_importing_load_function_invalid_path_format() -> None:
    """Path without a dot should raise ImportError."""

    with pytest.raises(ImportError):
        importing_load_function("not_a_valid_path_format")


def test_importing_load_function_missing_module() -> None:
    """Missing module should raise ImportError (ModuleNotFoundError)."""

    with pytest.raises(ImportError):
        importing_load_function("missing_module_xyz.func")


def test_importing_load_function_missing_attribute() -> None:
    """Existing module but missing function should raise AttributeError."""

    with pytest.raises(AttributeError):
        importing_load_function("json.non_existing_function")
