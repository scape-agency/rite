# =============================================================================
# Test: types_to_bytes
# =============================================================================

"""
Tests for rite.conversion.types.types_to_bytes.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import os
import pathlib

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_bytes import (
    types_to_bytes,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_types_to_bytes_basic_and_passthrough() -> None:
    """Test bytes/bytearray passthrough and basic conversions."""
    data = b"hello"
    ba = bytearray(b"world")

    assert types_to_bytes(data) is data
    assert types_to_bytes(ba) is ba
    assert types_to_bytes(memoryview(b"view")) == b"view"
    assert types_to_bytes("text") == b"text"
    assert types_to_bytes(42) == b"42"


def test_types_to_bytes_strings_only_protects_numeric() -> None:
    """Test strings_only flag leaves protected numeric types unchanged."""
    value = 42

    assert types_to_bytes(value, strings_only=True) is value
    assert types_to_bytes(value, strings_only=False) == b"42"


def test_types_to_bytes_dunder_bytes_and_pathlike() -> None:
    """Test objects with __bytes__ and os.PathLike handling."""

    class CustomBytes:
        def __bytes__(self) -> bytes:  # noqa: D401
            """Return custom bytes."""

            return b"custom"

    obj = CustomBytes()
    assert types_to_bytes(obj) == b"custom"

    # Test PathLike object without __bytes__ method
    class CustomPath:
        def __init__(self, path: str):
            self.path = path

        def __fspath__(self) -> str:
            """Return filesystem path."""
            return self.path

    custom_path = CustomPath("test/path.txt")
    result = types_to_bytes(custom_path)
    assert isinstance(result, (bytes, bytearray))
    assert result.decode("utf-8") == "test/path.txt"


def test_types_to_bytes_fallback_to_str() -> None:
    """Test fallback conversion of objects without special handling."""

    # Object without __bytes__ method
    class CustomObject:
        def __str__(self) -> str:
            """Return string representation."""
            return "custom_object"

    obj = CustomObject()
    result = types_to_bytes(obj)
    assert result == b"custom_object"

    # List without special handling
    list_obj = [1, 2, 3]
    result = types_to_bytes(list_obj)
    assert result == b"[1, 2, 3]"
