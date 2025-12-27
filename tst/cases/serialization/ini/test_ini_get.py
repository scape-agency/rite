# =============================================================================
# Test: ini_get
# =============================================================================

"""
Tests for rite.serialization.ini.ini_get.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.ini.ini_get import (
    ini_get,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_ini_get(tmp_path) -> None:
    """Test ini_get() function."""
    # Import | Standard Library
    import configparser

    # Create a test INI file
    ini_file = tmp_path / "test.ini"
    config = configparser.ConfigParser()
    config["section1"] = {"key1": "value1", "key2": "value2"}
    with ini_file.open("w") as f:
        config.write(f)

    # Test getting existing value
    result = ini_get(str(ini_file), "section1", "key1")
    assert result == "value1"

    # Test getting non-existing key with default
    result = ini_get(str(ini_file), "section1", "missing", "default")
    assert result == "default"
