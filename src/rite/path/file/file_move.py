import shutil
from pathlib import Path


def move_file(directory_path: str, file_name: str, new_directory: str) -> None:
    """
    Moves a file from the current directory to a specified new directory.

    Args:
        directory_path (str): The path of the current directory.
        file_name (str): The name of the file to be moved.
        new_directory (str): The destination directory.

    Notes:
        - If the destination directory doesn't exist, it will be created.
        - Logs messages for success or failure.

    Raises:
        FileNotFoundError: If the file to move does not exist.
        OSError: If the file could not be moved.
    """
    src = Path(directory_path) / file_name
    dst_dir = Path(new_directory)
    dst = dst_dir / file_name

    try:
        if not src.is_file():
            raise FileNotFoundError(f"❌ File not found: {src}")

        dst_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        print(f"✅ File moved: {src} → {dst}")
    except Exception as e:
        print(f"❌ Error moving file '{file_name}': {e}")
        raise


# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "move_file",
]

# =============================================================================
# Examples
# =============================================================================

# move_file("/tmp/input", "data.csv", "/tmp/archive")
