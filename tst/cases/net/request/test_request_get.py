# =============================================================================
# Test: request_get
# =============================================================================

"""
Tests for rite.net.request.request_get.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.request.request_get import (
    request_get,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_request_get() -> None:
    """Test request_get() function."""
    # Import | Standard Library
    from unittest.mock import MagicMock, mock_open, patch
    from urllib.error import URLError

    # Test successful GET request with proper mock
    response_data = b"test response"
    with patch("rite.net.request.request_get.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = response_data
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        result = request_get("http://example.com")
        assert result == "test response"

    # Test with custom headers
    with patch("rite.net.request.request_get.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"test"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        request_get("http://example.com", headers={"User-Agent": "Test"})
        assert mock_urlopen.called

    # Test with timeout
    with patch("rite.net.request.request_get.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"test"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        request_get("http://example.com", timeout=10.0)
        assert mock_urlopen.called

    # Test URLError handling
    with patch(
        "rite.net.request.request_get.urlopen",
        side_effect=URLError("Connection failed"),
    ):
        with pytest.raises(URLError):
            request_get("http://invalid.example.com")

    # Test default timeout
    with patch("rite.net.request.request_get.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b"test"
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        mock_urlopen.return_value = mock_response

        request_get("http://example.com")
        assert mock_urlopen.called
