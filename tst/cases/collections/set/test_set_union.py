# =============================================================================
# Test: Set Union
# =============================================================================

"""Tests for rite.collections.set.set_union.
"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.set import set_union


class TestSetUnion:
    """Tests for set_union function."""

    def test_basic_union(self) -> None:
        """Test basic union of two sets."""
        result = set_union({1, 2}, {2, 3})
        assert result == {1, 2, 3}

    def test_union_three_sets(self) -> None:
        """Test union of three sets."""
        result = set_union({1, 2}, {2, 3}, {3, 4})
        assert result == {1, 2, 3, 4}

    def test_union_empty_sets(self) -> None:
        """Test union with empty sets."""
        result = set_union(set(), {1, 2})
        assert result == {1, 2}

    def test_union_all_empty(self) -> None:
        """Test union of all empty sets."""
        result = set_union(set(), set(), set())
        assert result == set()

    def test_union_no_arguments(self) -> None:
        """Test union with no arguments."""
        result = set_union()
        assert result == set()

    def test_union_single_set(self) -> None:
        """Test union with single set."""
        result = set_union({1, 2, 3})
        assert result == {1, 2, 3}

    def test_union_overlapping(self) -> None:
        """Test union with overlapping elements."""
        result = set_union({1, 2, 3}, {2, 3, 4}, {3, 4, 5})
        assert result == {1, 2, 3, 4, 5}

    def test_union_no_overlap(self) -> None:
        """Test union with no overlapping elements."""
        result = set_union({1, 2}, {3, 4}, {5, 6})
        assert result == {1, 2, 3, 4, 5, 6}

    def test_union_duplicate_sets(self) -> None:
        """Test union with duplicate sets."""
        result = set_union({1, 2}, {1, 2})
        assert result == {1, 2}

    def test_union_string_elements(self) -> None:
        """Test union with string elements."""
        result = set_union({"a", "b"}, {"b", "c"})
        assert result == {"a", "b", "c"}

    def test_union_mixed_types(self) -> None:
        """Test union with sets containing different comparable types."""
        result = set_union({1, "a"}, {2, "b"})
        assert result == {1, "a", 2, "b"}


class TestSetUnionEdgeCases:
    """Edge case tests for set_union."""

    def test_union_large_sets(self) -> None:
        """Test union with large sets."""
        set1 = set(range(1000))
        set2 = set(range(500, 1500))
        result = set_union(set1, set2)
        assert result == set(range(1500))

    def test_union_many_sets(self) -> None:
        """Test union of many sets."""
        sets = [{i} for i in range(10)]
        result = set_union(*sets)
        assert result == set(range(10))
