import os

def get_file_extension(filename):
    """
    Get the file extension from a given filename.

    Args:
        filename (str): The name or path of the file.

    Returns:
        str: The file extension (without the dot), or an empty string if no extension exists.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")
    
    # Use os.path.splitext to separate the filename and extension
    _, extension = os.path.splitext(filename)
    
    # Remove the leading dot and return
    return extension.lstrip('.')