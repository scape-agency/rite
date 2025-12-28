# =============================================================================
# Benchmark: Text Operations
# =============================================================================

"""
Benchmarks for rite.text module operations.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text import (
    char_frequency,
    sanitize,
    slugify,
    text_is_email,
    text_truncate,
    to_camel_case,
    to_kebab_case,
    to_pascal_case,
    to_snake_case,
)

# =============================================================================
# Benchmark Tests
# =============================================================================


def test_benchmark_slugify(benchmark):
    """Benchmark slug generation."""
    result = benchmark(slugify, "Hello World! This is a Test 123")
    assert isinstance(result, str)


def test_benchmark_to_snake_case(benchmark):
    """Benchmark snake_case conversion."""
    result = benchmark(to_snake_case, "HelloWorldTestCaseConversion")
    assert result == "hello_world_test_case_conversion"


def test_benchmark_to_camel_case(benchmark):
    """Benchmark camelCase conversion."""
    result = benchmark(to_camel_case, "hello_world_test_case")
    assert isinstance(result, str)


def test_benchmark_to_pascal_case(benchmark):
    """Benchmark PascalCase conversion."""
    result = benchmark(to_pascal_case, "hello_world_test_case")
    assert isinstance(result, str)


def test_benchmark_to_kebab_case(benchmark):
    """Benchmark kebab-case conversion."""
    result = benchmark(to_kebab_case, "helloWorldTestCase")
    assert isinstance(result, str)


def test_benchmark_char_frequency(benchmark):
    """Benchmark character frequency analysis."""
    text = "the quick brown fox jumps over the lazy dog" * 10
    result = benchmark(char_frequency, text)
    assert isinstance(result, dict)


def test_benchmark_text_is_email(benchmark):
    """Benchmark email validation."""
    result = benchmark(text_is_email, "test@example.com")
    assert result is True


def test_benchmark_text_truncate(benchmark):
    """Benchmark text truncation."""
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    result = benchmark(text_truncate, text, 20)
    assert isinstance(result, str)


def test_benchmark_sanitize_large_text(benchmark):
    """Benchmark text sanitization on large input."""
    text = "<p>Safe text</p>" * 100
    result = benchmark(sanitize, text)
    assert isinstance(result, str)
