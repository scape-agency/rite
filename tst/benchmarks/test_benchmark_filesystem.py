# =============================================================================
# Benchmark: Filesystem Operations
# =============================================================================

"""
Benchmarks for rite.filesystem module operations.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem import (
    file_read_bytes,
    file_read_text,
    file_write_bytes,
    file_write_text,
    path_clean,
    path_leaf,
    path_safe_join,
    path_secure,
)

# =============================================================================
# Benchmark Tests
# =============================================================================


def test_benchmark_file_write_text(benchmark, tmp_path: Path):
    """Benchmark text file writing."""
    file_path = tmp_path / "test.txt"
    content = "Test content line\n" * 100

    def write_text():
        file_write_text(file_path, content)

    benchmark(write_text)
    assert file_path.exists()


def test_benchmark_file_read_text(benchmark, tmp_path: Path):
    """Benchmark text file reading."""
    file_path = tmp_path / "test.txt"
    content = "Test content line\n" * 100
    file_write_text(file_path, content)

    result = benchmark(file_read_text, file_path)
    assert isinstance(result, str)


def test_benchmark_file_write_bytes(benchmark, tmp_path: Path):
    """Benchmark binary file writing."""
    file_path = tmp_path / "test.bin"
    data = b"Binary test data" * 100

    def write_bytes():
        file_write_bytes(file_path, data)

    benchmark(write_bytes)
    assert file_path.exists()


def test_benchmark_file_read_bytes(benchmark, tmp_path: Path):
    """Benchmark binary file reading."""
    file_path = tmp_path / "test.bin"
    data = b"Binary test data" * 100
    file_write_bytes(file_path, data)

    result = benchmark(file_read_bytes, file_path)
    assert isinstance(result, bytes)


def test_benchmark_path_clean(benchmark):
    """Benchmark path cleaning."""
    result = benchmark(path_clean, "/path/to/../somewhere/./file.txt")
    assert isinstance(result, str)


def test_benchmark_path_secure(benchmark):
    """Benchmark path security check."""
    result = benchmark(path_secure, "/safe/base/path", "../../etc/passwd")
    assert isinstance(result, str)


def test_benchmark_path_safe_join(benchmark):
    """Benchmark safe path joining."""
    result = benchmark(path_safe_join, "/base/path", "subdir", "file.txt")
    assert isinstance(result, str)


def test_benchmark_path_leaf(benchmark):
    """Benchmark path leaf extraction."""
    result = benchmark(path_leaf, "/path/to/some/file.txt")
    assert result == "file.txt"
