import os

def delete_empty_directory(path):
    """
    Delete an empty directory.

    Args:
        path (str): The path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: If the directory is not empty or cannot be deleted.
        ValueError: If the provided path is not a directory.

    Returns:
        bool: True if the directory was successfully deleted.
    """
    # Validate input path exists and is a directory
    if not os.path.exists(path):
        raise FileNotFoundError(f"The directory '{path}' does not exist.")
    
    if not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a directory.")
    
    # Check if directory is empty
    if os.listdir(path):
        raise OSError(f"The directory '{path}' is not empty.")
    
    try:
        os.rmdir(path)
        return True
    except PermissionError:
        raise OSError(f"Permission denied: Cannot delete directory '{path}'.")