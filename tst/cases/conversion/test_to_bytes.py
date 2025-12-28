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


def test_to_bytes_with_different_encodings() -> None:
    """Test to_bytes with different character encodings."""
    # UTF-8 (default)
    assert to_bytes("hello") == b"hello"
    assert to_bytes("hello", encoding="utf-8") == b"hello"

    # UTF-16
    utf16_bytes = to_bytes("hello", encoding="utf-16")
    assert isinstance(utf16_bytes, bytes)
    assert utf16_bytes.decode("utf-16") == "hello"

    # Latin-1
    assert to_bytes("café", encoding="latin-1") == b"caf\xe9"


def test_to_bytes_with_unicode_characters() -> None:
    """Test to_bytes with various unicode characters."""
    # Emoji
    emoji = "🎉"
    result = to_bytes(emoji)
    assert result == emoji.encode("utf-8")
    assert result.decode("utf-8") == emoji

    # Chinese characters
    chinese = "你好"
    result = to_bytes(chinese)
    assert result == chinese.encode("utf-8")
    assert result.decode("utf-8") == chinese

    # Mixed
    mixed = "Hello 世界 🌍"
    result = to_bytes(mixed)
    assert result.decode("utf-8") == mixed


def test_to_bytes_error_handling() -> None:
    """Test to_bytes error handling with strict and replace modes."""
    text_with_special = "hello\ufffd"  # Contains replacement char

    # Strict mode (should work)
    result = to_bytes(text_with_special, errors="strict")
    assert isinstance(result, bytes)

    # Replace mode
    result = to_bytes(text_with_special, errors="replace")
    assert isinstance(result, bytes)


def test_to_bytes_protected_types_without_strings_only() -> None:
    """Test that protected types are converted to strings when strings_only=False."""
    # None
    result = to_bytes(None, strings_only=False)
    assert result == b"None"

    # Float
    result = to_bytes(3.14, strings_only=False)
    assert result == b"3.14"

    # Boolean
    result = to_bytes(True, strings_only=False)
    assert result == b"True"

    # List
    result = to_bytes([1, 2, 3], strings_only=False)
    assert result == b"[1, 2, 3]"


def test_to_bytes_complex_objects() -> None:
    """Test to_bytes with complex object types."""
    # Dictionary
    d = {"key": "value"}
    result = to_bytes(d)
    assert isinstance(result, bytes)
    assert b"key" in result

    # Custom class without __bytes__
    class NoBytes:
        def __str__(self) -> str:
            return "custom_str"

    obj = NoBytes()
    result = to_bytes(obj)
    assert result == b"custom_str"


def test_to_bytes_pathlike_with_bytes_result() -> None:
    """Test PathLike that returns bytes from os.fspath."""
    # Create a proper PathLike object
    path = pathlib.Path("test.txt")
    result = to_bytes(path)
    assert isinstance(result, bytes)
    assert b"test.txt" in result


def test_to_bytes_memoryview_conversion() -> None:
    """Test memoryview conversion to bytes."""
    data = b"test data"
    mv = memoryview(data)

    result = to_bytes(mv)
    assert result == data
    assert isinstance(result, bytes)


def test_to_bytes_bytearray_preservation() -> None:
    """Test that bytearray is returned as-is."""
    ba = bytearray(b"test")
    result = to_bytes(ba)
    assert result is ba
    assert isinstance(result, bytearray)


def test_to_bytes_empty_string() -> None:
    """Test to_bytes with empty string."""
    result = to_bytes("")
    assert result == b""


def test_to_bytes_long_string() -> None:
    """Test to_bytes with long string."""
    long_str = "a" * 10000
    result = to_bytes(long_str)
    assert len(result) == 10000
    assert result == b"a" * 10000
