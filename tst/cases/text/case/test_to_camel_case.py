# =============================================================================
# Test: to_camel_case
# =============================================================================

"""
Tests for rite.text.case.to_camel_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_camel_case import (
    to_camel_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_camel_case_basic() -> None:
    """Test to_camel_case() function with basic input."""
    result = to_camel_case("hello world")
    assert result == "helloWorld"


def test_to_camel_case_single_word() -> None:
    """Test to_camel_case with single word."""
    assert to_camel_case("hello") == "hello"


def test_to_camel_case_multiple_words() -> None:
    """Test to_camel_case with multiple words."""
    assert to_camel_case("hello world test") == "helloWorldTest"


def test_to_camel_case_empty_string() -> None:
    """Test to_camel_case with empty string."""
    assert to_camel_case("") == ""


def test_to_camel_case_special_chars() -> None:
    """Test to_camel_case with special characters."""
    assert to_camel_case("hello-world") == "helloWorld"
    assert to_camel_case("hello_world") == "helloWorld"
    assert to_camel_case("hello.world") == "helloWorld"


def test_to_camel_case_uppercase_start() -> None:
    """Test to_camel_case with uppercase starting letters."""
    assert to_camel_case("Hello World") == "helloWorld"
    assert to_camel_case("HELLO WORLD") == "helloWorld"


def test_to_camel_case_numbers() -> None:
    """Test to_camel_case with numbers."""
    assert to_camel_case("test 123 abc") == "test123Abc"


def test_to_camel_case_mixed_separators() -> None:
    """Test to_camel_case with mixed separators."""
    assert to_camel_case("hello-world_test.case") == "helloWorldTestCase"


def test_to_camel_case_consecutive_separators() -> None:
    """Test to_camel_case with consecutive separators."""
    assert to_camel_case("hello---world") == "helloWorld"


def test_to_camel_case_leading_trailing_spaces() -> None:
    """Test to_camel_case with leading and trailing spaces."""
    result = to_camel_case("  hello world  ")
    assert "hello" in result.lower() and "world" in result.lower()
