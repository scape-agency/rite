# =============================================================================
# Test: validation_is_ipv4
# =============================================================================

"""
Tests for rite.net.validation.validation_is_ipv4.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.validation.validation_is_ipv4 import (
    validation_is_ipv4,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_validation_is_ipv4_valid_address() -> None:
    """Test validation_is_ipv4 with valid IPv4 address."""
    assert validation_is_ipv4("192.168.1.1") is True


def test_validation_is_ipv4_localhost() -> None:
    """Test validation_is_ipv4 with localhost."""
    assert validation_is_ipv4("127.0.0.1") is True


def test_validation_is_ipv4_zeros() -> None:
    """Test validation_is_ipv4 with all zeros."""
    assert validation_is_ipv4("0.0.0.0") is True


def test_validation_is_ipv4_max_values() -> None:
    """Test validation_is_ipv4 with maximum valid values."""
    assert validation_is_ipv4("255.255.255.255") is True


def test_validation_is_ipv4_out_of_range() -> None:
    """Test validation_is_ipv4 with out of range values."""
    assert validation_is_ipv4("256.1.1.1") is False
    assert validation_is_ipv4("1.1.1.256") is False


def test_validation_is_ipv4_incomplete() -> None:
    """Test validation_is_ipv4 with incomplete address."""
    assert validation_is_ipv4("192.168.1") is False
    assert validation_is_ipv4("192.168") is False


def test_validation_is_ipv4_too_many_octets() -> None:
    """Test validation_is_ipv4 with too many octets."""
    assert validation_is_ipv4("192.168.1.1.1") is False


def test_validation_is_ipv4_not_an_ip() -> None:
    """Test validation_is_ipv4 with non-IP string."""
    assert validation_is_ipv4("not an ip") is False


def test_validation_is_ipv4_empty_string() -> None:
    """Test validation_is_ipv4 with empty string."""
    assert validation_is_ipv4("") is False


def test_validation_is_ipv4_with_spaces() -> None:
    """Test validation_is_ipv4 with spaces."""
    assert validation_is_ipv4(" 192.168.1.1") is False
    assert validation_is_ipv4("192.168.1.1 ") is False


@pytest.mark.parametrize(
    "ip,expected",
    [
        ("10.0.0.1", True),
        ("172.16.0.1", True),
        ("8.8.8.8", True),
        ("1.2.3", False),
        ("1.2.3.4.5", False),
        ("a.b.c.d", False),
    ],
)
def test_validation_is_ipv4_parametrized(ip: str, expected: bool) -> None:
    """Test validation_is_ipv4 with various inputs."""
    assert validation_is_ipv4(ip) is expected
