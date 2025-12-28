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
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            assert instance is not None
            assert instance.db_path == tmp.name

    def test_execute_query(self) -> None:
        """Test SQLiteServer.execute_query() method."""
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query("CREATE TABLE test (id INTEGER, name TEXT)")
            instance.execute_query("INSERT INTO test VALUES (1, 'test')")
            # Should not raise

    def test_fetch_all(self) -> None:
        """Test SQLiteServer.fetch_all() method."""
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query("CREATE TABLE test (id INTEGER, name TEXT)")
            instance.execute_query("INSERT INTO test VALUES (1, 'test1')")
            instance.execute_query("INSERT INTO test VALUES (2, 'test2')")
            result = instance.fetch_all("SELECT * FROM test")
            assert len(result) == 2

    def test_fetch_one(self) -> None:
        """Test SQLiteServer.fetch_one() method."""
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query("CREATE TABLE test (id INTEGER, name TEXT)")
            instance.execute_query("INSERT INTO test VALUES (1, 'test')")
            result = instance.fetch_one("SELECT * FROM test WHERE id=1")
            assert result is not None

    def test_insert(self) -> None:
        """Test SQLiteServer.insert() method."""
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query("CREATE TABLE test (id INTEGER, name TEXT)")
            instance.insert("test", {"id": 1, "name": "test"})
            result = instance.fetch_all("SELECT * FROM test")
            assert len(result) == 1

    def test_update(self) -> None:
        """Test SQLiteServer.update() method."""
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query("CREATE TABLE test (id INTEGER, name TEXT)")
            instance.execute_query("INSERT INTO test VALUES (1, 'test')")
            instance.update("test", {"name": "updated"}, "id=1")
            result = instance.fetch_one("SELECT name FROM test WHERE id=1")
            assert result[0] == "updated"

    def test_delete(self) -> None:
        """Test SQLiteServer.delete() method."""
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query("CREATE TABLE test (id INTEGER, name TEXT)")
            instance.execute_query("INSERT INTO test VALUES (1, 'test')")
            instance.delete("test", "id=1")
            result = instance.fetch_all("SELECT * FROM test")
            assert len(result) == 0

    def test_transaction(self) -> None:
        """Test SQLiteServer.transaction() method."""
        # Import | Standard Library
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query("CREATE TABLE test (id INTEGER, name TEXT)")
            queries = [
                ("INSERT INTO test VALUES (?, ?)", (1, "test1")),
                ("INSERT INTO test VALUES (?, ?)", (2, "test2")),
            ]
            instance.transaction(queries)
            result = instance.fetch_all("SELECT * FROM test")
            assert len(result) == 2

    def test_transaction_rollback_on_error(self) -> None:
        """Test SQLiteServer.transaction() rolls back on error."""
        # Import | Standard Library
        import sqlite3
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            instance = SQLiteServer(tmp.name)
            instance.execute_query(
                "CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)"
            )
            instance.execute_query("INSERT INTO test VALUES (1, 'test1')")
            queries = [
                ("INSERT INTO test VALUES (?, ?)", (2, "test2")),
                # This should fail due to duplicate primary key
                ("INSERT INTO test VALUES (?, ?)", (1, "duplicate")),
            ]
            with pytest.raises(sqlite3.Error):
                instance.transaction(queries)
            # Check that first insert was rolled back
            result = instance.fetch_all("SELECT * FROM test")
            assert len(result) == 1


# =============================================================================
# Test Functions
# =============================================================================


def test_test() -> None:
    """Test test() function - skipped as it's for manual testing."""
    # The test() function is intended for manual testing with example usage
    pytest.skip("Test not implemented - test() is for manual testing")
