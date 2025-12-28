# =============================================================================
# Test: to_bytes
# =============================================================================

"""
Tests for rite.conversion.to_bytes.
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
from rite.conversion.to_bytes import to_bytes

# =============================================================================
# Test Functions
# =============================================================================


class CustomBytes:
    """Helper class implementing __bytes__ for testing."""

    def __bytes__(self) -> bytes:  # pragma: no cover - trivial
        return b"custom"


def test_to_bytes_passthrough_and_basic_types() -> None:
    """Return bytes-like objects as-is and encode strings/objects."""
    b = b"data"
    ba = bytearray(b"data")

    assert to_bytes(b) is b
    assert to_bytes(ba) is ba

    mv = memoryview(b"view")
    assert to_bytes(mv) == b"view"

    assert to_bytes("hello") == b"hello"
    assert to_bytes(123) == b"123"


def test_to_bytes_strings_only_uses_is_protected_type() -> None:
    """When strings_only is True, protected types are returned unchanged."""
    value = 42
    assert to_bytes(value, strings_only=True) is value
    assert to_bytes(value, strings_only=False) == b"42"


def test_to_bytes_uses_dunder_bytes_and_pathlike() -> None:
    """Support __bytes__ protocol and os.PathLike instances."""
    obj = CustomBytes()
    assert to_bytes(obj) == b"custom"

    path = pathlib.Path("some") / "path.txt"
    as_bytes = to_bytes(path)
    assert isinstance(as_bytes, (bytes, bytearray))
    assert as_bytes.decode("utf-8") == os.fspath(path)
