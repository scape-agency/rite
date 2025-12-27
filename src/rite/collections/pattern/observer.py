# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Observer Pattern
================

Implementation of the Observer design pattern for event-driven programming.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from abc import ABC, abstractmethod
from typing import Any

# =============================================================================
# Classes
# =============================================================================


class Observer(ABC):
    """
    Observer Abstract Base Class
    =============================

    Base class for observers in the Observer pattern.

    """

    @abstractmethod
    def update(
        self, observable: Observable, *args: Any, **kwargs: Any
    ) -> None:
        """
        Called when the observed object changes.

        Args:
        ----
            observable: The observable object that changed.
            *args: Positional arguments from the notification.
            **kwargs: Keyword arguments from the notification.

        """


class Observable:
    """
    Observable Class
    ================

    Base class for observable objects in the Observer pattern.

    """

    def __init__(self) -> None:
        """Initialize an observable object."""
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Attach an observer.

        Args:
        ----
            observer: The observer to attach.

        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detach an observer.

        Args:
        ----
            observer: The observer to detach.

        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, *args: Any, **kwargs: Any) -> None:
        """
        Notify all observers of a change.

        Args:
        ----
            *args: Positional arguments to pass to observers.
            **kwargs: Keyword arguments to pass to observers.

        """
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

    def get_observer_count(self) -> int:
        """
        Get the number of attached observers.

        Returns:
        -------
            int: Number of observers.

        """
        return len(self._observers)


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "Observer",
    "Observable",
]
