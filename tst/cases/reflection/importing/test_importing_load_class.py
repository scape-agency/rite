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

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.importing.importing_load_class import (
    ClassImportError,
    importing_load_class,
)

# =============================================================================
# Test Class: ClassImportError
# =============================================================================


class TestClassImportError:
    """Tests for ClassImportError class."""

    def test_instantiation(self) -> None:
        """Test ClassImportError can be instantiated."""
        instance = ClassImportError("message")
        assert isinstance(instance, ClassImportError)
        assert isinstance(instance, ImportError)
        assert "message" in str(instance)


# =============================================================================
# Test Functions
# =============================================================================


def test_importing_load_class_valid_paths() -> None:
    """Test importing_load_class() with valid class paths."""

    ordered_dict_cls = importing_load_class("collections.OrderedDict")
    # Import | Standard Library
    from collections import OrderedDict

    assert ordered_dict_cls is OrderedDict

    path_cls = importing_load_class("pathlib.Path")
    # Import | Standard Library
    from pathlib import Path

    assert path_cls is Path


def test_importing_load_class_invalid_path_format() -> None:
    """Invalid path format should raise ClassImportError."""

    with pytest.raises(ClassImportError) as exc_info:
        importing_load_class("NotAValidPath")

    assert "Invalid path format" in str(exc_info.value)


def test_importing_load_class_missing_module() -> None:
    """Missing module should raise ClassImportError."""

    with pytest.raises(ClassImportError) as exc_info:
        importing_load_class("missing_module_xyz.MissingClass")

    assert "Module 'missing_module_xyz' not found" in str(exc_info.value)


def test_importing_load_class_missing_class() -> None:
    """Existing module but missing class should raise ClassImportError."""

    with pytest.raises(ClassImportError) as exc_info:
        importing_load_class("pathlib.MissingClass")

    assert "has no class 'MissingClass'" in str(exc_info.value)
