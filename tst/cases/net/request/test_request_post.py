# =============================================================================
# Test: request_post
# =============================================================================

"""
Tests for rite.net.request.request_post.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.request.request_post import (
    request_post,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_request_post() -> None:
    """Test request_post() function."""
    # Import | Standard Library
    from unittest.mock import MagicMock, patch
    from urllib.error import URLError

    # Test successful POST request with dict data
    with patch("rite.net.request.request_post.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"success"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        result = request_post("http://example.com", data={"key": "value"})
        assert result == "success"

    # Test POST with bytes data
    with patch("rite.net.request.request_post.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"response"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        result = request_post("http://example.com", data=b"raw bytes")
        assert result == "response"

    # Test POST with no data
    with patch("rite.net.request.request_post.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"ok"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        result = request_post("http://example.com")
        assert result == "ok"

    # Test with custom headers
    with patch("rite.net.request.request_post.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"test"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        request_post(
            "http://example.com",
            data={"a": "1"},
            headers={"Content-Type": "application/json"},
        )
        assert mock_urlopen.called

    # Test with timeout
    with patch("rite.net.request.request_post.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"test"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        request_post("http://example.com", timeout=5.0)
        assert mock_urlopen.called

    # Test URLError handling
    with patch(
        "rite.net.request.request_post.urlopen",
        side_effect=URLError("Connection failed"),
    ):
        with pytest.raises(URLError):
            request_post("http://invalid.example.com")
