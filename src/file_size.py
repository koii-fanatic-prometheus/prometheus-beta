import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        int: The size of the file in bytes.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
        IsADirectoryError: If the path is a directory, not a file.
    """
    # Validate input is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Check if file exists and is a file
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise IsADirectoryError(f"Path is not a file: {file_path}")

    # Get and return file size
    return os.path.getsize(file_path)