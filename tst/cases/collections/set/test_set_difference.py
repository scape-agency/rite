# =============================================================================
# Test: Set Difference
# =============================================================================

"""Tests for rite.collections.set.set_difference."""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.set import set_difference


class TestSetDifference:
    """Tests for set_difference function."""

    def test_basic_difference(self) -> None:
        """Test basic difference of two sets."""
        result = set_difference({1, 2, 3}, {2})
        assert result == {1, 3}

    def test_difference_multiple_sets(self) -> None:
        """Test difference with multiple sets to subtract."""
        result = set_difference({1, 2, 3}, {2}, {3})
        assert result == {1}

    def test_difference_no_subtraction(self) -> None:
        """Test difference with no elements to subtract."""
        result = set_difference({1, 2, 3})
        assert result == {1, 2, 3}

    def test_difference_empty_first(self) -> None:
        """Test difference with empty first set."""
        result = set_difference(set(), {1, 2})
        assert result == set()

    def test_difference_empty_second(self) -> None:
        """Test difference with empty set to subtract."""
        result = set_difference({1, 2, 3}, set())
        assert result == {1, 2, 3}

    def test_difference_no_overlap(self) -> None:
        """Test difference with no overlapping elements."""
        result = set_difference({1, 2, 3}, {4, 5, 6})
        assert result == {1, 2, 3}

    def test_difference_complete_overlap(self) -> None:
        """Test difference with complete overlap."""
        result = set_difference({1, 2, 3}, {1, 2, 3})
        assert result == set()

    def test_difference_string_elements(self) -> None:
        """Test difference with string elements."""
        result = set_difference({"a", "b", "c"}, {"b"})
        assert result == {"a", "c"}

    def test_difference_large_sets(self) -> None:
        """Test difference with large sets."""
        set1 = set(range(1000))
        set2 = set(range(500, 750))
        result = set_difference(set1, set2)
        assert result == set(range(500)) | set(range(750, 1000))

    def test_difference_multiple_subtractions(self) -> None:
        """Test difference with multiple subtractions."""
        result = set_difference({1, 2, 3, 4, 5}, {1}, {3}, {5})
        assert result == {2, 4}


class TestSetDifferenceEdgeCases:
    """Edge case tests for set_difference."""

    def test_difference_partial_overlap(self) -> None:
        """Test difference with partial overlap."""
        result = set_difference({1, 2, 3, 4}, {2, 3}, {3, 4})
        assert result == {1}

    def test_difference_zero_element(self) -> None:
        """Test difference including zero."""
        result = set_difference({0, 1, 2, 3}, {1, 2})
        assert result == {0, 3}

    def test_difference_single_element(self) -> None:
        """Test difference with single element sets."""
        result = set_difference({1}, {2}, {3})
        assert result == {1}
