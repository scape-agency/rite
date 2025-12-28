# =============================================================================
# Benchmark: Crypto Operations
# =============================================================================

"""
Benchmarks for rite.crypto module operations.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash import (
    hash_blake2b,
    hash_md5,
    hash_sha256,
)
from rite.crypto.uuid import (
    uuid_hex,
    uuid_random,
)
from rite.crypto.uuid.uuid_is_valid import is_valid_uuid

# =============================================================================
# Benchmark Tests
# =============================================================================


def test_benchmark_hash_sha256(benchmark):
    """Benchmark SHA-256 hashing."""
    data = "sensitive data to hash" * 10
    result = benchmark(hash_sha256, data)
    assert isinstance(result, str)


def test_benchmark_hash_md5(benchmark):
    """Benchmark MD5 hashing."""
    data = "data to hash with md5" * 10
    result = benchmark(hash_md5, data)
    assert isinstance(result, str)


def test_benchmark_hash_blake2b(benchmark):
    """Benchmark BLAKE2b hashing."""
    data = b"binary data for blake2b" * 10
    result = benchmark(hash_blake2b, data)
    assert isinstance(result, str)


def test_benchmark_uuid_random(benchmark):
    """Benchmark UUID generation."""
    result = benchmark(uuid_random)
    assert result is not None


def test_benchmark_uuid_hex(benchmark):
    """Benchmark UUID hex generation."""
    result = benchmark(uuid_hex)
    assert isinstance(result, str)
    assert len(result) == 32


def test_benchmark_uuid_is_valid(benchmark):
    """Benchmark UUID validation."""
    result = benchmark(is_valid_uuid, "550e8400-e29b-41d4-a716-446655440000")
    assert result is True
