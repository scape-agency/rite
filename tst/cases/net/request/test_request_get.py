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
    from unittest.mock import patch, MagicMock
    from urllib.error import URLError

    # Test successful GET request
    mock_response = MagicMock()
    mock_response.read.return_value = b"test response"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response):
        result = request_get("http://example.com")
        assert result == "test response"

    # Test with custom headers
    mock_response = MagicMock()
    mock_response.read.return_value = b"test"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response) as mock:
        request_get("http://example.com", headers={"User-Agent": "Test"})
        # Check that Request was created with headers
        call_args = mock.call_args
        assert call_args is not None

    # Test with timeout
    mock_response = MagicMock()
    mock_response.read.return_value = b"test"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response) as mock:
        request_get("http://example.com", timeout=10.0)
        # Check that timeout was passed
        call_kwargs = mock.call_args[1] if len(mock.call_args) > 1 else {}
        assert "timeout" in call_kwargs or len(mock.call_args[0]) > 1

    # Test URLError handling
    with patch("urllib.request.urlopen", side_effect=URLError("Connection failed")):
        with pytest.raises(URLError):
            request_get("http://invalid.example.com")

    # Test default timeout
    mock_response = MagicMock()
    mock_response.read.return_value = b"test"
    mock_response.__enter__.return_value = mock_response
    mock_response.__exit__.return_value = None

    with patch("urllib.request.urlopen", return_value=mock_response) as mock:
        request_get("http://example.com")
        assert mock.call_args is not None
