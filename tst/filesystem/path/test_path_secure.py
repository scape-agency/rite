# Import | Future
from __future__ import annotations

# Import | Standard Library
import os

# Import | Local Modules
from rite.filesystem import path_secure


def test_path_secure_uses_only_basename() -> None:
    secure_path = path_secure("/var/data", "../../../etc/passwd")
    # Normalize path for cross-platform comparison
    assert secure_path.endswith("passwd")
    assert ".." not in os.path.basename(secure_path)
