import logging
import shutil
from pathlib import Path


def delete_contents(
    folder: str | Path,
    *,
    dry_run: bool = False,
    verbose: bool = True,
) -> None:
    """
    Deletes all files and subdirectories inside a given folder.
    The folder itself is preserved.

    Args:
        folder (str | Path): The directory whose contents will be deleted.
        dry_run (bool): If True, shows what would be deleted without performing it.
        verbose (bool): If True, prints or logs deleted paths.
    """
    path = Path(folder)

    if not path.exists():
        raise FileNotFoundError(f"Folder does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")

    for item in path.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                if dry_run:
                    print(f"[DRY-RUN] Would delete file: {item}")
                else:
                    item.unlink()
                    if verbose:
                        print(f"🗑️ Deleted file: {item}")
            elif item.is_dir():
                if dry_run:
                    print(f"[DRY-RUN] Would delete directory: {item}")
                else:
                    shutil.rmtree(item)
                    if verbose:
                        print(f"🗑️ Deleted folder: {item}")

        except Exception as e:
            logging.error(f"❌ Failed to delete {item}: {e}")


# def delete_contents(self, folder):
#     """
#     Deletes all contents (files and subdirectories) within a specified
#     folder.

#     Parameters:
#     folder (str): The path to the folder whose contents are to be deleted.

#     Notes:
#     This method removes both files and subdirectories within the specified
#     folder. It handles symbolic links and regular files differently to
#     ensure safe deletion.

#     Raises:
#     Exception: If an error occurs during the deletion process.
#     """
#     for filename in os.listdir(folder):
#         file_path = os.path.join(folder, filename)
#         try:
#             if os.path.isfile(file_path) or os.path.islink(file_path):
#                 os.unlink(file_path)
#             elif os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#         except Exception as e:
#             print(f"Failed to delete {file_path}. Reason: {e}")

# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "delete_contents",
]

# =============================================================================
# Example Usage
# =============================================================================

# Normal use
delete_contents("output/images")

# Dry run (just shows what would be deleted)
delete_contents("output/images", dry_run=True)

# Silent version (no console output)
delete_contents("output/images", verbose=False)
