# =============================================================================
# Test: server_sqlite
# =============================================================================

"""
Tests for rite.net.servers.server_sqlite.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.servers.server_sqlite import (
    SQLiteServer,
    test,
)

# =============================================================================
# Test Class: SQLiteServer
# =============================================================================


class TestSQLiteServer:
    """Tests for SQLiteServer class."""

    def test_instantiation(self) -> None:
        """Test SQLiteServer can be instantiated."""
        # TODO: Implement test
        instance = SQLiteServer()
        assert instance is not None

    def test_execute_query(self) -> None:
        """Test SQLiteServer.execute_query() method."""
        # TODO: Implement test
        instance = SQLiteServer()
        # result = instance.execute_query()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_fetch_all(self) -> None:
        """Test SQLiteServer.fetch_all() method."""
        # TODO: Implement test
        instance = SQLiteServer()
        # result = instance.fetch_all()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_fetch_one(self) -> None:
        """Test SQLiteServer.fetch_one() method."""
        # TODO: Implement test
        instance = SQLiteServer()
        # result = instance.fetch_one()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_insert(self) -> None:
        """Test SQLiteServer.insert() method."""
        # TODO: Implement test
        instance = SQLiteServer()
        # result = instance.insert()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_update(self) -> None:
        """Test SQLiteServer.update() method."""
        # TODO: Implement test
        instance = SQLiteServer()
        # result = instance.update()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_delete(self) -> None:
        """Test SQLiteServer.delete() method."""
        # TODO: Implement test
        instance = SQLiteServer()
        # result = instance.delete()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_transaction(self) -> None:
        """Test SQLiteServer.transaction() method."""
        # TODO: Implement test
        instance = SQLiteServer()
        # result = instance.transaction()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Functions
# =============================================================================


def test_test() -> None:
    """Test test() function."""
    # TODO: Implement test
    # result = test(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")
