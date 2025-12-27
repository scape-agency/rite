# =============================================================================
# Test: importing_load_class
# =============================================================================

"""
Tests for rite.reflection.importing.importing_load_class.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.reflection.importing.importing_load_class import (
    importing_load_class,
    ClassImportError,
)


# =============================================================================
# Test Class: ClassImportError
# =============================================================================


class TestClassImportError:
    """Tests for ClassImportError class."""

    def test_instantiation(self) -> None:
        """Test ClassImportError can be instantiated."""
        # TODO: Implement test
        instance = ClassImportError()
        assert instance is not None


# =============================================================================
# Test Functions
# =============================================================================


def test_importing_load_class() -> None:
    """Test importing_load_class() function."""
    # TODO: Implement test
    # result = importing_load_class(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")

