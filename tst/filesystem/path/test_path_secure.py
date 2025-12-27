from __future__ import annotations

from rite.filesystem import path_secure


def test_path_secure_uses_only_basename() -> None:
    secure_path = path_secure("/var/data", "../../../etc/passwd")
    assert secure_path.endswith("/passwd")
    assert "/.." not in secure_path
