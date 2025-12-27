# =============================================================================
# Test: server_http
# =============================================================================

"""
Tests for rite.net.servers.server_http.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.net.servers.server_http import (
    test,
    BaseHTTPServer,
)


# =============================================================================
# Test Class: BaseHTTPServer
# =============================================================================


class TestBaseHTTPServer:
    """Tests for BaseHTTPServer class."""

    def test_instantiation(self) -> None:
        """Test BaseHTTPServer can be instantiated."""
        # TODO: Implement test
        instance = BaseHTTPServer()
        assert instance is not None

    def test_do_get(self) -> None:
        """Test BaseHTTPServer.do_get() method."""
        # TODO: Implement test
        instance = BaseHTTPServer()
        # result = instance.do_get()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_do_post(self) -> None:
        """Test BaseHTTPServer.do_post() method."""
        # TODO: Implement test
        instance = BaseHTTPServer()
        # result = instance.do_post()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_run(self) -> None:
        """Test BaseHTTPServer.run() method."""
        # TODO: Implement test
        instance = BaseHTTPServer()
        # result = instance.run()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Functions
# =============================================================================


def test_test() -> None:
    """Test test() function."""
    # TODO: Implement test
    # result = test(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")

