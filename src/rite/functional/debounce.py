# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Debounce Decorator
==================

Delays function execution by a specified wait time.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import time
from typing import Any, Callable, TypeVar

T = TypeVar("T")


# =============================================================================
# Functions
# =============================================================================


def debounce(
    wait_time: float,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to debounce a function call.

    Args:
        wait_time: Time to wait in seconds before executing the function

    Returns:
        Decorated function that delays execution

    Example:
        >>> @debounce(0.5)
        ... def greet():
        ...     return "Hello"
        >>> greet()  # Waits 0.5 seconds before returning
        'Hello'
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapped(*args: Any, **kwargs: Any) -> T:
            time.sleep(wait_time)
            return func(*args, **kwargs)

        return wrapped

    return decorator


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "debounce",
]
