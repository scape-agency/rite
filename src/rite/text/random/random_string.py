# -*- coding: utf-8 -*-
from __future__ import annotations
import secrets
import string

def random_string(length: int = 16, charset: str = string.ascii_letters + string.digits) -> str:
    """Generate a secure random string."""
    return "".join(secrets.choice(charset) for _ in range(length))


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "random_string",
]
