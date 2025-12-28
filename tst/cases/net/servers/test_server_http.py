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
import io
from unittest.mock import MagicMock, patch

# Import | Local Modules
from rite.net.servers.server_http import (
    BaseHTTPServer,
)

# =============================================================================
# Test Class: BaseHTTPServer
# =============================================================================


class TestBaseHTTPServer:
    """Tests for BaseHTTPServer class."""

    def test_class_exists(self) -> None:
        """Test BaseHTTPServer class exists and is properly defined."""
        assert BaseHTTPServer is not None
        assert hasattr(BaseHTTPServer, "do_get")
        assert hasattr(BaseHTTPServer, "do_post")
        assert hasattr(BaseHTTPServer, "_send_response")
        assert hasattr(BaseHTTPServer, "_handle_404")
        assert hasattr(BaseHTTPServer, "run")

    def test_run_method_is_callable(self) -> None:
        """Test BaseHTTPServer.run() method is callable."""
        assert callable(BaseHTTPServer.run)

    def test_do_get_root_path(self) -> None:
        """Test do_get for root path."""
        handler = MagicMock(spec=BaseHTTPServer)
        handler.path = "/"
        handler.headers = {}
        handler.wfile = io.BytesIO()

        BaseHTTPServer.do_get(handler)

        handler._send_response.assert_called_once()
        call_args = handler._send_response.call_args
        assert call_args[0][0] == 200
        assert "Welcome" in call_args[0][1]

    def test_do_get_info_path(self) -> None:
        """Test do_get for /info path."""
        handler = MagicMock(spec=BaseHTTPServer)
        handler.path = "/info?key=value"
        handler.headers = {}
        handler.wfile = io.BytesIO()

        BaseHTTPServer.do_get(handler)

        handler._send_response.assert_called_once()
        call_args = handler._send_response.call_args
        assert call_args[0][0] == 200

    def test_do_get_404(self) -> None:
        """Test do_get for unknown path returns 404."""
        handler = MagicMock(spec=BaseHTTPServer)
        handler.path = "/unknown"
        handler.headers = {}
        handler.wfile = io.BytesIO()

        BaseHTTPServer.do_get(handler)

        handler._handle_404.assert_called_once()

    def test_do_post(self) -> None:
        """Test do_post method."""
        handler = MagicMock(spec=BaseHTTPServer)
        handler.path = "/submit"
        handler.headers = {"Content-Length": "8"}
        handler.rfile = io.BytesIO(b"key=test")
        handler.wfile = io.BytesIO()

        BaseHTTPServer.do_post(handler)

        handler._send_response.assert_called_once()
        call_args = handler._send_response.call_args
        assert call_args[0][0] == 200

    def test_send_response(self) -> None:
        """Test _send_response helper method."""
        handler = MagicMock(spec=BaseHTTPServer)
        handler.wfile = io.BytesIO()

        BaseHTTPServer._send_response(
            handler, 200, "Test content", "text/plain"
        )

        handler.send_response.assert_called_once_with(200)
        handler.send_header.assert_called_once_with(
            "Content-type", "text/plain"
        )
        handler.end_headers.assert_called_once()

    def test_send_response_bytes_content(self) -> None:
        """Test _send_response with bytes content."""
        handler = MagicMock(spec=BaseHTTPServer)
        handler.wfile = io.BytesIO()

        BaseHTTPServer._send_response(
            handler, 200, b"byte content", "application/octet-stream"
        )

        handler.send_response.assert_called_once_with(200)

    def test_handle_404(self) -> None:
        """Test _handle_404 helper method."""
        handler = MagicMock(spec=BaseHTTPServer)
        handler.wfile = io.BytesIO()

        BaseHTTPServer._handle_404(handler)

        handler._send_response.assert_called_once()
        call_args = handler._send_response.call_args
        assert call_args[0][0] == 404
        assert "404" in call_args[0][1]

    @patch("rite.net.servers.server_http.HTTPServer")
    @patch("rite.net.servers.server_http.logging")
    def test_run_with_keyboard_interrupt(
        self, mock_logging: MagicMock, mock_server_class: MagicMock
    ) -> None:
        """Test run method handles KeyboardInterrupt."""
        mock_server = MagicMock()
        mock_server.serve_forever.side_effect = KeyboardInterrupt()
        mock_server_class.return_value = mock_server

        # Call run - it should handle KeyboardInterrupt gracefully
        BaseHTTPServer.run(server_class=mock_server_class, port=8888)

        mock_server.server_close.assert_called_once()
