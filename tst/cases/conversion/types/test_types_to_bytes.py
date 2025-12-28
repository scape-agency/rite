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

    path = pathlib.Path("some/path.txt")
    result = types_to_bytes(path)
    assert isinstance(result, (bytes, bytearray))
    assert result.decode("utf-8") == os.fspath(path)
