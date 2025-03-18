import os
import shutil
from datetime import datetime

def create_file_backup(source_path, backup_dir=None):
    """
    Create a backup of a given file with a timestamp.

    Args:
        source_path (str): Path to the source file to be backed up.
        backup_dir (str, optional): Directory to store backups. 
                                    If None, backup in same directory as source.

    Returns:
        str: Path to the created backup file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If source_path is a directory, not a file.
        PermissionError: If there are insufficient permissions to read/write.
    """
    # Validate source file exists and is a file
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path must be a file, not a directory: {source_path}")

    # Determine backup directory
    if backup_dir is None:
        backup_dir = os.path.dirname(source_path) or '.'
    
    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)

    # Generate backup filename with timestamp 
    filename = os.path.basename(source_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{filename}_{timestamp}"
    backup_path = os.path.join(backup_dir, backup_filename)

    # Copy the file
    try:
        shutil.copy2(source_path, backup_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when backing up file: {source_path}")

    return backup_path