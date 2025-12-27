

# =============================================================================
# Docstring
# =============================================================================

"""
Network Module
==============

This module provides network utilities similar to Python's
http.server and urllib modules.

Functions will include:
- HTTP server utilities
- SQLite server/utilities

Example:
    >>> from rite.net import http_server
    >>> server = http_server(port=8000)

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local
from .http_server import BaseHTTPServer
from .sqlite_server import SQLiteServer

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "BaseHTTPServer",
    "SQLiteServer",
]
