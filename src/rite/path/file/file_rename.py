from pathlib import Path


def rename_file(
    directory_path: str, old_file_name: str, new_file_name: str
) -> None:
    """
    Renames a file within the specified directory.

    Args:
        directory_path (str): The path to the directory containing the file.
        old_file_name (str): The current name of the file.
        new_file_name (str): The new name for the file.

    Raises:
        FileNotFoundError: If the file to rename does not exist.
        OSError: If the rename operation fails.
    """
    dir_path = Path(directory_path)
    old_file = dir_path / old_file_name
    new_file = dir_path / new_file_name

    try:
        if old_file.is_file():
            old_file.rename(new_file)
            print(f"✅ File renamed from {old_file} to {new_file}")
        else:
            raise FileNotFoundError(f"❌ File not found: {old_file}")
    except Exception as e:
        print(f"❌ Error renaming file: {e}")
        raise


# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "rename_file",
]

# =============================================================================
# Examples
# =============================================================================

# rename_file("/data/exports", "draft.txt", "final.txt")
