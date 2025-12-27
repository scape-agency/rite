# =============================================================================
# Test: observer
# =============================================================================

"""
Tests for rite.collections.pattern.observer.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.pattern.observer import (
    Observable,
    Observer,
)

# =============================================================================
# Test Class: Observer
# =============================================================================


class TestObserver:
    """Tests for Observer class."""

    def test_instantiation(self) -> None:
        """Test Observer can be instantiated."""
        # TODO: Implement test
        instance = Observer()
        assert instance is not None

    def test_update(self) -> None:
        """Test Observer.update() method."""
        # TODO: Implement test
        instance = Observer()
        # result = instance.update()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Class: Observable
# =============================================================================


class TestObservable:
    """Tests for Observable class."""

    def test_instantiation(self) -> None:
        """Test Observable can be instantiated."""
        # TODO: Implement test
        instance = Observable()
        assert instance is not None

    def test_observers(self) -> None:
        """Test Observable.observers() method."""
        # TODO: Implement test
        instance = Observable()
        # result = instance.observers()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_attach(self) -> None:
        """Test Observable.attach() method."""
        # TODO: Implement test
        instance = Observable()
        # result = instance.attach()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_detach(self) -> None:
        """Test Observable.detach() method."""
        # TODO: Implement test
        instance = Observable()
        # result = instance.detach()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_notify(self) -> None:
        """Test Observable.notify() method."""
        # TODO: Implement test
        instance = Observable()
        # result = instance.notify()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_get_observer_count(self) -> None:
        """Test Observable.get_observer_count() method."""
        # TODO: Implement test
        instance = Observable()
        # result = instance.get_observer_count()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_clear_observers(self) -> None:
        """Test Observable.clear_observers() method."""
        # TODO: Implement test
        instance = Observable()
        # result = instance.clear_observers()
        # assert result is not None
        pytest.skip("Test not implemented")
