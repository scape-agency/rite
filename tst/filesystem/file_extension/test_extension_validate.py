# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem import extension_validate


def test_extension_validate_allows_and_rejects() -> None:
    extension_validate("jpg", allowed=["jpg", "png"])

    with pytest.raises(ValueError):
        extension_validate("!")

    with pytest.raises(ValueError):
        extension_validate("exe", allowed=["jpg", "png"])
