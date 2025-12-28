# Import | Future
from __future__ import annotations

# Import | Standard Library
import io
from typing import Any

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem import file_size_to_string


class MockFileWithSize:
    """Mock file object with size attribute."""

    def __init__(self, size: int) -> None:
        self.size = size

    def tell(self) -> int:
        return 0

    def seek(self, pos: int, whence: int = 0) -> int:
        return 0


class MockFileWithInvalidSize:
    """Mock file object with invalid size attribute."""

    @property
    def size(self) -> str:
        return "not a number"

    def tell(self) -> int:
        return 0

    def seek(self, pos: int, whence: int = 0) -> int:
        return 0


class MockFileWithBrokenMethods:
    """Mock file object where tell/seek raise errors."""

    def tell(self) -> int:
        raise OSError("Cannot tell")

    def seek(self, pos: int, whence: int = 0) -> int:
        raise OSError("Cannot seek")


class MockFileWithMissingMethods:
    """Mock file object with missing tell/seek methods."""

    pass


def test_file_size_to_string_from_stream_units() -> None:
    """Test file_size_to_string with BytesIO stream."""
    buffer = io.BytesIO(b"1234567890")  # 10 bytes
    size_string = file_size_to_string(buffer)
    assert any(unit in size_string for unit in ("B", "KB", "MB"))


def test_file_size_to_string_bytes_unit() -> None:
    """Test file_size_to_string with small files in bytes."""
    buffer = io.BytesIO(b"hello")  # 5 bytes
    result = file_size_to_string(buffer)
    assert "5 B" == result


def test_file_size_to_string_kilobytes() -> None:
    """Test file_size_to_string with KB files."""
    data = b"x" * 1024  # 1 KB
    buffer = io.BytesIO(data)
    result = file_size_to_string(buffer)
    assert "1.00 KB" == result


def test_file_size_to_string_megabytes() -> None:
    """Test file_size_to_string with MB files."""
    data = b"x" * (1024 * 1024)  # 1 MB
    buffer = io.BytesIO(data)
    result = file_size_to_string(buffer)
    assert "1.00 MB" == result


def test_file_size_to_string_gigabytes() -> None:
    """Test file_size_to_string with GB files."""
    # Don't create actual GB data, use mock instead
    mock_file = MockFileWithSize(1024 * 1024 * 1024)  # 1 GB
    result = file_size_to_string(mock_file)
    assert "1.00 GB" == result


def test_file_size_to_string_terabytes() -> None:
    """Test file_size_to_string with TB files."""
    mock_file = MockFileWithSize(1024 * 1024 * 1024 * 1024)  # 1 TB
    result = file_size_to_string(mock_file)
    assert "1.00 TB" == result


def test_file_size_to_string_petabytes() -> None:
    """Test file_size_to_string with PB files."""
    mock_file = MockFileWithSize(1024 * 1024 * 1024 * 1024 * 1024)  # 1 PB
    result = file_size_to_string(mock_file)
    assert "1.00 PB" == result


def test_file_size_to_string_zero_bytes() -> None:
    """Test file_size_to_string with empty file."""
    buffer = io.BytesIO(b"")
    result = file_size_to_string(buffer)
    assert "0 B" == result


def test_file_size_to_string_fractional_kb() -> None:
    """Test file_size_to_string with fractional KB."""
    data = b"x" * 1536  # 1.5 KB
    buffer = io.BytesIO(data)
    result = file_size_to_string(buffer)
    assert "1.50 KB" == result


def test_file_size_to_string_fractional_mb() -> None:
    """Test file_size_to_string with fractional MB."""
    data = b"x" * (1024 * 1024 + 512 * 1024)  # 1.5 MB
    buffer = io.BytesIO(data)
    result = file_size_to_string(buffer)
    assert "1.50 MB" == result


def test_file_size_to_string_with_size_attribute() -> None:
    """Test file_size_to_string using size attribute."""
    mock_file = MockFileWithSize(2048)  # 2 KB
    result = file_size_to_string(mock_file)
    assert "2.00 KB" == result


def test_file_size_to_string_with_invalid_size_attribute() -> None:
    """Test file_size_to_string falls back when size is invalid."""
    mock_file = MockFileWithInvalidSize()
    result = file_size_to_string(mock_file)
    # Should fall back to tell/seek, getting "Unknown size" since they
    # return 0
    assert isinstance(result, str)


def test_file_size_to_string_seek_and_tell() -> None:
    """Test file_size_to_string correctly uses seek and tell."""
    buffer = io.BytesIO(b"x" * 100)
    buffer.seek(50)  # Move to middle
    result = file_size_to_string(buffer)
    # Should determine size correctly and restore position
    assert "100 B" == result
    assert buffer.tell() == 50  # Position should be restored


def test_file_size_to_string_with_broken_methods() -> None:
    """Test file_size_to_string returns Unknown size on error."""
    mock_file = MockFileWithBrokenMethods()
    result = file_size_to_string(mock_file)
    assert result == "Unknown size"


def test_file_size_to_string_with_missing_methods() -> None:
    """Test file_size_to_string with file missing tell/seek methods."""
    mock_file = MockFileWithMissingMethods()
    result = file_size_to_string(mock_file)
    assert result == "Unknown size"


def test_file_size_to_string_with_type_error_in_size() -> None:
    """Test file_size_to_string handles TypeError in int() conversion."""

    class MockFileWithNonIntSize:
        @property
        def size(self) -> list[int]:
            return [1, 2, 3]

    mock_file = MockFileWithNonIntSize()  # type: ignore
    result = file_size_to_string(mock_file)
    assert isinstance(result, str)


def test_file_size_to_string_negative_size() -> None:
    """Test file_size_to_string with negative size."""
    mock_file = MockFileWithSize(-100)
    result = file_size_to_string(mock_file)
    assert result == "0 B"  # Negative sizes should return 0 B
