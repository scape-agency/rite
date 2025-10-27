from pathlib import Path


def delete_file(directory_path: str, file_name: str) -> None:
    """
    Deletes a file within the specified directory.

    Args:
        directory_path (str): The path to the directory containing the file.
        file_name (str): The name of the file to delete.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If the file could not be deleted due to an OS error.
    """
    file_path = Path(directory_path) / file_name

    try:
        if file_path.is_file():
            file_path.unlink()
            print(f"✅ File deleted: {file_path}")
        else:
            raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        print(f"❌ Error deleting file: {e}")
        raise


# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "delete_file",
]

# =============================================================================
# Examples
# =============================================================================

# delete_file("/home/user/documents", "old_data.txt")
