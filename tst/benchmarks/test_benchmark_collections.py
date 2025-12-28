# =============================================================================
# Benchmark: Collections Operations
# =============================================================================

"""
Benchmarks for rite.collections module operations.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.dict import (
    dict_deep_get,
    dict_deep_set,
    dict_merge,
)
from rite.collections.list import (
    list_chunk,
    list_flatten,
    list_partition,
    list_unique,
)

# =============================================================================
# Benchmark Tests
# =============================================================================


def test_benchmark_list_unique(benchmark):
    """Benchmark list unique operation."""
    data = list(range(100)) * 10  # Duplicate data
    result = benchmark(list_unique, data)
    assert len(result) == 100


def test_benchmark_list_flatten(benchmark):
    """Benchmark list flattening."""
    data = [[i, i + 1, i + 2] for i in range(0, 100, 3)]
    result = benchmark(list_flatten, data)
    assert isinstance(result, list)


def test_benchmark_list_chunk(benchmark):
    """Benchmark list chunking."""
    data = list(range(1000))
    result = benchmark(list_chunk, data, 10)
    assert isinstance(result, list)


def test_benchmark_list_partition(benchmark):
    """Benchmark list partitioning."""
    data = list(range(100))
    result = benchmark(list_partition, data, lambda x: x % 2 == 0)
    assert isinstance(result, tuple)


def test_benchmark_dict_deep_get(benchmark):
    """Benchmark deep dictionary access."""
    data = {"level1": {"level2": {"level3": {"value": "found"}}}}
    result = benchmark(
        dict_deep_get, data, ["level1", "level2", "level3", "value"]
    )
    assert result == "found"


def test_benchmark_dict_deep_set(benchmark):
    """Benchmark deep dictionary setting."""
    data = {}

    def deep_set():
        dict_deep_set(data.copy(), "level1.level2.level3.value", "test")

    benchmark(deep_set)


def test_benchmark_dict_merge(benchmark):
    """Benchmark dictionary merging."""
    dict1 = {f"key_{i}": i for i in range(50)}
    dict2 = {f"key_{i}": i * 2 for i in range(25, 75)}
    result = benchmark(dict_merge, dict1, dict2)
    assert isinstance(result, dict)
