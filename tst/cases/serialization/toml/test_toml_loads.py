# =============================================================================
# Test: toml_loads
# =============================================================================

"""
Tests for rite.serialization.toml.toml_loads.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import builtins
from unittest.mock import patch

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.toml.toml_loads import (
    toml_loads,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_toml_loads() -> None:
    """Test toml_loads() function."""
    # Test basic parse
    toml_string = """
[section]
key = "value"
number = 42
"""
    result = toml_loads(toml_string)
    assert result["section"]["key"] == "value"
    assert result["section"]["number"] == 42

    # Test simple key-value
    result = toml_loads('key = "value"')
    assert result["key"] == "value"

    # Test multiple sections
    toml_string = """
[database]
host = "localhost"
port = 5432

[server]
address = "0.0.0.0"
port = 8080
"""
    result = toml_loads(toml_string)
    assert result["database"]["host"] == "localhost"
    assert result["database"]["port"] == 5432
    assert result["server"]["address"] == "0.0.0.0"
    assert result["server"]["port"] == 8080

    # Test various data types
    toml_string = """
string = "hello"
integer = 123
float = 3.14
boolean = true
array = [1, 2, 3]
"""
    result = toml_loads(toml_string)
    assert result["string"] == "hello"
    assert result["integer"] == 123
    assert result["float"] == 3.14
    assert result["boolean"] is True
    assert result["array"] == [1, 2, 3]

    # Test nested sections
    toml_string = """
[database]
server = "127.0.0.1"

[database.connection]
timeout = 30
retries = 3
"""
    result = toml_loads(toml_string)
    assert result["database"]["server"] == "127.0.0.1"
    assert result["database"]["connection"]["timeout"] == 30


def test_toml_loads_import_error() -> None:
    """Test toml_loads() raises ImportError when tomllib unavailable."""
    original_import = builtins.__import__

    def mock_import(name, *args, **kwargs):
        if name == "tomllib":
            raise ImportError("No module named 'tomllib'")
        return original_import(name, *args, **kwargs)

    with patch.object(builtins, "__import__", side_effect=mock_import):
        with pytest.raises(ImportError, match="tomllib requires Python 3.11"):
            toml_loads('key = "value"')
