# =============================================================================
# Test: Set Intersection
# =============================================================================

"""Tests for rite.collections.set.set_intersection."""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.set import set_intersection


class TestSetIntersection:
    """Tests for set_intersection function."""

    def test_basic_intersection(self) -> None:
        """Test basic intersection of two sets."""
        result = set_intersection({1, 2, 3}, {2, 3, 4})
        assert result == {2, 3}

    def test_intersection_three_sets(self) -> None:
        """Test intersection of three sets."""
        result = set_intersection({1, 2, 3}, {2, 3, 4}, {2, 3, 5})
        assert result == {2, 3}

    def test_intersection_no_common(self) -> None:
        """Test intersection with no common elements."""
        result = set_intersection({1, 2}, {3, 4})
        assert result == set()

    def test_intersection_empty_sets(self) -> None:
        """Test intersection with empty set."""
        result = set_intersection(set(), {1, 2})
        assert result == set()

    def test_intersection_no_arguments(self) -> None:
        """Test intersection with no arguments."""
        result = set_intersection()
        assert result == set()

    def test_intersection_single_set(self) -> None:
        """Test intersection with single set."""
        result = set_intersection({1, 2, 3})
        assert result == {1, 2, 3}

    def test_intersection_identical_sets(self) -> None:
        """Test intersection of identical sets."""
        result = set_intersection({1, 2, 3}, {1, 2, 3})
        assert result == {1, 2, 3}

    def test_intersection_subset(self) -> None:
        """Test intersection where one is subset of other."""
        result = set_intersection({1, 2, 3, 4}, {2, 3})
        assert result == {2, 3}

    def test_intersection_string_elements(self) -> None:
        """Test intersection with string elements."""
        result = set_intersection({"a", "b", "c"}, {"b", "c", "d"})
        assert result == {"b", "c"}

    def test_intersection_large_sets(self) -> None:
        """Test intersection of large sets."""
        set1 = set(range(1000))
        set2 = set(range(500, 1500))
        result = set_intersection(set1, set2)
        assert result == set(range(500, 1000))

    def test_intersection_many_sets(self) -> None:
        """Test intersection of many sets."""
        sets = [
            {1, 2, 3, 4, 5},
            {1, 2, 3, 4},
            {1, 2, 3},
            {1, 2},
        ]
        result = set_intersection(*sets)
        assert result == {1, 2}


class TestSetIntersectionEdgeCases:
    """Edge case tests for set_intersection."""

    def test_intersection_single_element_overlap(self) -> None:
        """Test intersection with single element overlap."""
        result = set_intersection({1, 2, 3}, {3, 4, 5}, {3, 6, 7})
        assert result == {3}

    def test_intersection_zero_element(self) -> None:
        """Test intersection including zero."""
        result = set_intersection({0, 1, 2}, {0, 2, 3})
        assert result == {0, 2}
