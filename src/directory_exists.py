import os

def check_directory_exists(path):
    """
    Check if a directory exists at the given path.

    Args:
        path (str): The path to the directory to check.

    Returns:
        bool: True if the directory exists, False otherwise.

    Raises:
        TypeError: If the path is not a string.
    """
    # Check if path is a string
    if not isinstance(path, str):
        raise TypeError("Path must be a string")

    # Normalize the path to handle different path formats
    normalized_path = os.path.normpath(path)

    # Check if path exists and is a directory
    return os.path.isdir(normalized_path)