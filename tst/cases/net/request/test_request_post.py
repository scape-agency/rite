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
    from unittest.mock import patch, MagicMock
    from urllib.error import URLError

    # Test successful POST request with dict data
    mock_response = MagicMock()
    mock_response.read.return_value = b"success"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response):
        result = request_post("http://example.com", data={"key": "value"})
        assert result == "success"

    # Test POST with bytes data
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response):
        result = request_post("http://example.com", data=b"raw bytes")
        assert result == "response"

    # Test POST with no data
    mock_response = MagicMock()
    mock_response.read.return_value = b"ok"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response):
        result = request_post("http://example.com")
        assert result == "ok"

    # Test with custom headers
    mock_response = MagicMock()
    mock_response.read.return_value = b"test"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response):
        request_post(
            "http://example.com",
            data={"a": "1"},
            headers={"Content-Type": "application/json"},
        )

    # Test with timeout
    mock_response = MagicMock()
    mock_response.read.return_value = b"test"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response) as mock:
        request_post("http://example.com", timeout=5.0)
        assert mock.call_args is not None

    # Test URLError handling
    with patch("urllib.request.urlopen", side_effect=URLError("Connection failed")):
        with pytest.raises(URLError):
            request_post("http://invalid.example.com")
