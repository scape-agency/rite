# =============================================================================
# Test: toml_load
# =============================================================================

"""
Tests for rite.serialization.toml.toml_load.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.toml.toml_load import (
    toml_load,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_toml_load(tmp_path: pytest.TempPathFactory) -> None:
    """Test toml_load() function."""
    # Import | Standard Library
    from pathlib import Path
    import tempfile

    # Create temporary TOML file
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".toml", delete=False
    ) as f:
        f.write(
            """
[section]
key = "value"
number = 42

[database]
host = "localhost"
port = 5432
"""
        )
        temp_path = f.name

    try:
        # Test basic load
        result = toml_load(temp_path)
        assert result["section"]["key"] == "value"
        assert result["section"]["number"] == 42
        assert result["database"]["host"] == "localhost"
        assert result["database"]["port"] == 5432

        # Test with Path object
        result = toml_load(Path(temp_path))
        assert isinstance(result, dict)
        assert "section" in result
    finally:
        Path(temp_path).unlink()
