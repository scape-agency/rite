from pathlib import Path
from typing import List, Optional


def list_files(
    rootdir: str | Path,
    pattern: Optional[str] = None,
    recursive: bool = False,
    extensions: Optional[List[str]] = None,
) -> List[Path]:
    """
    List all files in the given directory.

    Args:
        rootdir (str | Path): The directory to search in.
        pattern (Optional[str]): Optional glob pattern (e.g., '*.txt' or 'data_*').
        recursive (bool): If True, searches recursively through subdirectories.
        extensions (Optional[List[str]]): Optional list of file extensions to include (e.g., ['.py', '.txt']).

    Returns:
        List[Path]: A list of Path objects for the matching files.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the provided path is not a directory.
    """
    root_path = Path(rootdir)

    if not root_path.exists():
        raise FileNotFoundError(f"Directory not found: {root_path}")

    if not root_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {root_path}")

    # Select appropriate iterator
    iterator = root_path.rglob("*") if recursive else root_path.iterdir()

    # Filter files
    files = [p for p in iterator if p.is_file()]

    # Apply optional pattern matching
    if pattern:
        files = [f for f in files if f.match(pattern)]

    # Filter by extensions if provided
    if extensions:
        normalized_exts = {
            e.lower() if e.startswith(".") else f".{e.lower()}"
            for e in extensions
        }
        files = [f for f in files if f.suffix.lower() in normalized_exts]

    return files


# def list_files(rootdir, ext=None):
#     """List the files in DIR, ext=optional."""
#     files = os.listdir(rootdir)
#     files = [f for f in files if os.path.isfile(os.path.join(rootdir, f))]
#     if ext:
#         files = [f for f in files if ext == pathlib.Path(f).suffix]
#     return files

# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "list_files",
]

# =============================================================================
# Example Usage
# =============================================================================

# List all files in a folder
files = list_files("data")
print(files)

# List recursively
all_files = list_files("data", recursive=True)
print(all_files)

# List only text files
txt_files = list_files("data", extensions=[".txt"])
print(txt_files)

# List only files matching a pattern
matching = list_files("data", pattern="report_*")
print(matching)
