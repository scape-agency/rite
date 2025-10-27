# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Folder Create Module
====================

This module provides functions to create directories.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path
from typing import List

# Import | Libraries

# Import | Local Modules

# =============================================================================
# Functions
# =============================================================================


def create_directory(
    path: str | Path,
    mode: int = 0o777,
) -> Path:
    """
    Ensures the given directory exists and returns the Path object.

    Args:
        path (str | Path): The directory path to create.
        mode (int): Permissions mode (default: 0o777).

    Returns:
        Path: A pathlib.Path object representing the created or existing
            directory.

    """

    # Convert to Path object if a string is provided
    if isinstance(path, str):
        path = Path(path)

    # Create the directory if it doesn't exist with the specified mode
    path.mkdir(
        parents=True,
        exist_ok=True,
        mode=mode,
    )

    # Return the Path object
    return path


# def create_subfolder(self, subfolder_name):
#     """
#     Creates a subfolder within the current directory.

#     Parameters:
#     subfolder_name (str): The name of the subfolder to create.

#     Raises:
#     Exception: If the subfolder could not be created.
#     """
#     path = os.path.join(self.directory_path, subfolder_name)
#     try:
#         os.makedirs(path, exist_ok=True)
#         print(f"Subfolder created: {path}")
#     except Exception as e:
#         print(f"Error creating subfolder: {e}")

# =============================================================================
# Exports
# =============================================================================

__all__: List[str] = [
    "create_directory",
]


# =============================================================================
# Example Usage
# =============================================================================

output_path = create_directory("output/images")
print(f"Directory ready at: {output_path.resolve()}")
