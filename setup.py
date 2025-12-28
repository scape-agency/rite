"""Setup script for rite package.

This setup.py is provided for backward compatibility with tools that don't
support pyproject.toml yet. The canonical build configuration is in pyproject.toml.
"""

# Pylint struggles to resolve setuptools in some environments; keep a safe import
try:  # type: ignore
    # Import | Libraries
    from setuptools import setup  # pylint: disable=import-error
except ImportError:  # pragma: no cover
    # Minimal fallback to make static analyzers happy; runtime should have setuptools
    def setup(**_kwargs):  # type: ignore
        raise RuntimeError("setuptools is required to build this package")


# Read dependencies from pyproject.toml is handled by setuptools
# when using PEP 517/518 build backend
setup()
