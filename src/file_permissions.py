import os
import stat

def change_file_permissions(file_path, permissions):
    """
    Change the permissions of a file.

    Args:
        file_path (str): Path to the file whose permissions are to be changed.
        permissions (int): Octal representation of the desired file permissions 
                           (e.g., 0o755 for read/write/execute for owner, 
                           read/execute for group and others).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If permissions are not provided as an integer.
        ValueError: If permissions are not a valid octal representation.
    """
    # Validate input parameters
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    if not isinstance(permissions, int):
        raise TypeError("Permissions must be an integer (octal representation)")
    
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate permissions are in valid octal range (0-0o777)
    if permissions < 0 or permissions > 0o777:
        raise ValueError("Permissions must be between 0 and 0o777")
    
    # Change file permissions
    try:
        os.chmod(file_path, permissions)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    
    return True