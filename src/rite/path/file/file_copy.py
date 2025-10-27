import shutil
from pathlib import Path


def copy_file(src: Path, dst: Path, overwrite: bool = True) -> None:
    """
    Copy a file from source to destination.

    Args:
        src (Path): Source file path.
        dst (Path): Destination file path.
        overwrite (bool): Whether to overwrite the destination if it exists.

    Raises:
        FileNotFoundError: If the source file does not exist.
        FileExistsError: If the destination file exists and overwrite is False.
        IOError: For other I/O related errors.

    """

    if not src.exists():
        raise FileNotFoundError(f"Source file does not exist: {src}")

    if dst.exists() and not overwrite:
        raise FileExistsError(f"Destination file already exists: {dst}")

    dst.parent.mkdir(
        parents=True, exist_ok=True
    )  # Ensure destination folder exists

    shutil.copyfile(src, dst)


# def copy_file(self, file_name, new_directory):
#     """
#     Copies a file from the current directory to a specified new directory.

#     Parameters:
#     file_name (str): The name of the file to be copied.
#     new_directory (str): The path to the directory where the file should
#     be copied.

#     Notes:
#     If the new directory does not exist, it is created.
#     If the file does not exist in the current directory, an error message
#     is displayed.

#     Raises:
#     Exception: If an error occurs during the file copying process.
#     """
#     source = os.path.join(self.directory_path, file_name)
#     destination = os.path.join(new_directory, file_name)

#     try:
#         if os.path.isfile(source):
#             os.makedirs(new_directory, exist_ok=True)
#             shutil.copy2(source, destination)
#             print(f"File copied: {source} -> {destination}")
#         else:
#             print(f"File not found: {source}")
#     except Exception as e:
#         print(f"Error copying file: {e}")


# =============================================================================
# Example Usage
# =============================================================================

# from pathlib import Path

# copy_file(Path("data/input.txt"), Path("backup/input_backup.txt"))
