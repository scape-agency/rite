# =============================================================================
# Test: ini_set
# =============================================================================

"""
Tests for rite.serialization.ini.ini_set.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.ini.ini_set import (
    ini_set,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_ini_set(tmp_path) -> None:
    """Test ini_set() function."""
    # Import | Standard Library
    import configparser

    # Create a test INI file
    ini_file = tmp_path / "test.ini"
    config = configparser.ConfigParser()
    config["section1"] = {"key1": "value1"}
    with ini_file.open("w") as f:
        config.write(f)

    # Test setting a value
    ini_set(str(ini_file), "section1", "key1", "new_value")

    # Verify the value was updated
    result_config = configparser.ConfigParser()
    result_config.read(str(ini_file))
    assert result_config["section1"]["key1"] == "new_value"


def test_ini_set_existing_file(tmp_path) -> None:
    """Test ini_set reads existing file (line 62)."""
    # Import | Standard Library
    import configparser

    # Create a test INI file with existing content
    ini_file = tmp_path / "existing.ini"
    config = configparser.ConfigParser()
    config["section1"] = {"key1": "original"}
    config["section2"] = {"key2": "keep_this"}
    with ini_file.open("w") as f:
        config.write(f)

    # Update a value - should preserve other sections
    ini_set(str(ini_file), "section1", "key1", "updated")

    # Verify file was read and other sections preserved
    result = configparser.ConfigParser()
    result.read(str(ini_file))
    assert result["section1"]["key1"] == "updated"
    assert result["section2"]["key2"] == "keep_this"


def test_ini_set_new_section(tmp_path) -> None:
    """Test ini_set creates new section if needed."""
    # Import | Standard Library
    import configparser

    ini_file = tmp_path / "new.ini"
    ini_set(str(ini_file), "new_section", "new_key", "new_value")

    result = configparser.ConfigParser()
    result.read(str(ini_file))
    assert result["new_section"]["new_key"] == "new_value"
