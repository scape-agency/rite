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
from rite.collections.pattern.observer import Observable, Observer

# =============================================================================
# Test Class: Observer
# =============================================================================


class TestObserver:
    """Tests for Observer class."""

    def test_instantiation(self) -> None:
        """Test Observer can be instantiated."""
        instance = Observer()
        assert instance is not None

    def test_update(self) -> None:
        """Test Observer.update() method."""
        instance = Observer()
        with pytest.raises(NotImplementedError):
            instance.update(None)


# =============================================================================
# Test Class: Observable
# =============================================================================


class TestObservable:
    """Tests for Observable class."""

    def test_instantiation(self) -> None:
        """Test Observable can be instantiated."""
        instance = Observable()
        assert instance.observers == ()

    def test_observers(self) -> None:
        """Test Observable.observers() method."""
        instance = Observable()
        assert isinstance(instance.observers, tuple)
        assert len(instance.observers) == 0

    def test_attach(self) -> None:
        """Test Observable.attach() method."""

        class _Observer(Observer):
            def update(self, observable, *args, **kwargs):  # type: ignore[override]
                self.called = True  # pragma: no cover - side effect only

        observable = Observable()
        observer = _Observer()

        observable.attach(observer)
        assert observer in observable.observers

        # Attaching the same observer twice should not duplicate it
        observable.attach(observer)
        assert observable.get_observer_count() == 1

    def test_detach(self) -> None:
        """Test Observable.detach() method."""

        class _Observer(Observer):
            def update(self, observable, *args, **kwargs):  # type: ignore[override]
                pass

        observable = Observable()
        observer = _Observer()
        observable.attach(observer)
        observable.detach(observer)

        assert observer not in observable.observers

        # Detaching a non-existent observer should be a no-op
        observable.detach(observer)

    def test_notify(self) -> None:
        """Test Observable.notify() method."""

        class _Observer(Observer):
            def __init__(self) -> None:
                self.notifications: list[
                    tuple[Observable | None, tuple, dict]
                ] = []

            def update(  # type: ignore[override]
                self,
                observable,
                *args,
                **kwargs,
            ) -> None:
                self.notifications.append((observable, args, kwargs))

        observable = Observable()
        observer = _Observer()
        observable.attach(observer)

        observable.notify("event", key="value")

        assert len(observer.notifications) == 1
        subject, args, kwargs = observer.notifications[0]
        assert subject is observable
        assert args == ("event",)
        assert kwargs == {"key": "value"}

    def test_get_observer_count(self) -> None:
        """Test Observable.get_observer_count() method."""
        observable = Observable()
        assert observable.get_observer_count() == 0

        class _Observer(Observer):
            def update(self, observable, *args, **kwargs):  # type: ignore[override]
                pass

        observable.attach(_Observer())
        observable.attach(_Observer())
        assert observable.get_observer_count() == 2

    def test_clear_observers(self) -> None:
        """Test Observable.clear_observers() method."""
        observable = Observable()

        class _Observer(Observer):
            def update(self, observable, *args, **kwargs):  # type: ignore[override]
                pass

        observable.attach(_Observer())
        observable.attach(_Observer())
        assert observable.get_observer_count() == 2

        observable.clear_observers()
        assert observable.get_observer_count() == 0
