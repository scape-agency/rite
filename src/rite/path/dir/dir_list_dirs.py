from pathlib import Path
from typing import List, Optional


def list_dirs(
    rootdir: str | Path,
    pattern: Optional[str] = None,
    recursive: bool = False,
) -> List[Path]:
    """
    Lists all subdirectories inside a given directory.

    Args:
        rootdir (str | Path): The directory to search.
        pattern (Optional[str]): Optional glob pattern to filter directories (e.g., 'data*').
        recursive (bool): If True, searches recursively through all subfolders.

    Returns:
        List[Path]: A list of Path objects representing found directories.
    """

    root_path = Path(rootdir)

    if not root_path.exists():
        raise FileNotFoundError(f"Directory not found: {root_path}")

    if not root_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {root_path}")

    if recursive:
        dirs = [p for p in root_path.rglob("*") if p.is_dir()]

    else:
        dirs = [p for p in root_path.iterdir() if p.is_dir()]

    if pattern:
        dirs = [d for d in dirs if d.match(pattern)]

    return dirs


# def list_dirs(rootdir):
#     """List directories in DIR."""
#     dirs = []
#     for file in os.listdir(rootdir):
#         d = os.path.join(rootdir, file)
#         if os.path.isdir(d):
#             dirs.append(file)
#     return dirs


# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "list_dirs",
]


# =============================================================================
# Example Usage
# =============================================================================

# List all subdirectories (non-recursive)
example_dirs = list_dirs("data")
print(example_dirs)

# List recursively
all_dirs = list_dirs("data", recursive=True)
print(all_dirs)

# List only directories starting with "test"
filtered_dirs = list_dirs("data", pattern="test*")
print(filtered_dirs)
