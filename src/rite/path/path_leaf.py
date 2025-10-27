from pathlib import Path


def path_leaf(path: str) -> str:
    """
    Returns the last part (leaf) of a given file path.

    Args:
        path (str): The input file path.

    Returns:
        str: The leaf name (file or folder name) of the path.
    """
    return Path(path).name


# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "path_leaf",
]

# =============================================================================
# Examples
# =============================================================================

# print(path_leaf("/some/folder/file.txt"))  # Outputs: file.txt
# print(path_leaf("C:\\Users\\Name\\Documents"))  # Outputs: Documents
