# =============================================================================
# Benchmark: Conversion Operations
# =============================================================================

"""
Benchmarks for rite.conversion module operations.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types import (
    types_to_bool,
    types_to_float,
    types_to_int,
    types_to_str,
)

# =============================================================================
# Benchmark Tests
# =============================================================================


def test_benchmark_types_to_bool(benchmark):
    """Benchmark boolean conversion."""
    result = benchmark(types_to_bool, "yes")
    assert result is True


def test_benchmark_types_to_int(benchmark):
    """Benchmark integer conversion."""
    result = benchmark(types_to_int, "12345")
    assert result == 12345


def test_benchmark_types_to_float(benchmark):
    """Benchmark float conversion."""
    result = benchmark(types_to_float, "123.45")
    assert result == 123.45


def test_benchmark_types_to_str(benchmark):
    """Benchmark string conversion."""
    result = benchmark(types_to_str, 12345)
    assert result == "12345"


def test_benchmark_types_to_bool_batch(benchmark):
    """Benchmark batch boolean conversions."""
    values = ["yes", "no", "true", "false", "1", "0"] * 10

    def convert_batch():
        return [types_to_bool(v) for v in values]

    result = benchmark(convert_batch)
    assert isinstance(result, list)


def test_benchmark_types_to_int_batch(benchmark):
    """Benchmark batch integer conversions."""
    values = [str(i) for i in range(100)]

    def convert_batch():
        return [types_to_int(v) for v in values]

    result = benchmark(convert_batch)
    assert len(result) == 100
