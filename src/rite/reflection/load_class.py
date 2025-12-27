

# =============================================================================
# Docstring
# =============================================================================

"""
Dynamic Class Loading
====================

Dynamically import classes from module paths.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from importlib import import_module

# =============================================================================
# Exceptions
# =============================================================================


class ClassImportError(ImportError):
    """Raised when a class cannot be dynamically imported."""


# =============================================================================
# Functions
# =============================================================================


def load_class(path: str) -> type:
    """
    Dynamically import a class from a given module path.

    Args:
        path: The fully qualified module path of the class
              (e.g., "mypackage.mymodule.MyClass")

    Returns:
        The loaded class object

    Raises:
        ClassImportError: If the module or class cannot be imported

    Example:
        >>> MyClass = load_class("collections.OrderedDict")
        >>> isinstance(MyClass(), dict)
        True
    """
    try:
        module_path, class_name = path.rsplit(".", 1)
    except ValueError as exc:
        raise ClassImportError(
            f"Invalid path format: '{path}'. Expected format 'module.ClassName'."
        ) from exc

    try:
        module = import_module(module_path)
    except ModuleNotFoundError as exc:
        raise ClassImportError(
            f"Error importing module '{module_path}': {exc}"
        ) from exc

    try:
        cls = getattr(module, class_name)
    except AttributeError as exc:
        raise ClassImportError(
            f"Module '{module_path}' does not define a class named '{class_name}'."
        ) from exc

    return cls


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "ClassImportError",
    "load_class",
]
