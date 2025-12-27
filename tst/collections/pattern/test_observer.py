# -*- coding: utf-8 -*-

"""Tests for Observer pattern."""

import pytest

from src.rite.collections.pattern import Observable, Observer


class ConcreteObserver(Observer):
    """Concrete observer for testing."""

    def __init__(self):
        self.notifications = []

    def update(self, observable, *args, **kwargs):
        """Record notifications."""
        self.notifications.append((observable, args, kwargs))


class TestObserver:
    """Test cases for Observer pattern."""

    def test_observable_init(self):
        """Test observable initialization."""
        observable = Observable()
        assert observable.observers == ()

    def test_attach_observer(self):
        """Test attaching an observer."""
        observable = Observable()
        observer = ConcreteObserver()

        observable.attach(observer)
        assert observer in observable.observers

    def test_attach_multiple_observers(self):
        """Test attaching multiple observers."""
        observable = Observable()
        observer1 = ConcreteObserver()
        observer2 = ConcreteObserver()

        observable.attach(observer1)
        observable.attach(observer2)

        assert observable.get_observer_count() == 2

    def test_detach_observer(self):
        """Test detaching an observer."""
        observable = Observable()
        observer = ConcreteObserver()

        observable.attach(observer)
        observable.detach(observer)

        assert observer not in observable.observers

    def test_detach_nonexistent_observer(self):
        """Test detaching non-existent observer."""
        observable = Observable()
        observer = ConcreteObserver()

        # Should not raise error
        observable.detach(observer)

    def test_notify_single_observer(self):
        """Test notifying a single observer."""
        observable = Observable()
        observer = ConcreteObserver()
        observable.attach(observer)

        observable.notify("test", key="value")

        assert len(observer.notifications) == 1
        subject, args, kwargs = observer.notifications[0]
        assert subject is observable
        assert args == ("test",)
        assert kwargs == {"key": "value"}

    def test_notify_multiple_observers(self):
        """Test notifying multiple observers."""
        observable = Observable()
        observer1 = ConcreteObserver()
        observer2 = ConcreteObserver()

        observable.attach(observer1)
        observable.attach(observer2)
        observable.notify("event")

        assert len(observer1.notifications) == 1
        assert len(observer2.notifications) == 1

    def test_notify_no_observers(self):
        """Test notifying with no observers."""
        observable = Observable()
        # Should not raise error
        observable.notify("event")

    def test_observer_abstract_update(self):
        """Test that Observer.update is abstract."""
        observer = Observer()

        with pytest.raises(NotImplementedError):
            observer.update(None)
