import os
import stat

def get_file_permissions(file_path):
    """
    Get the file permissions of a given file.

    Args:
        file_path (str): Path to the file whose permissions are to be retrieved.

    Returns:
        dict: A dictionary containing file permission details:
            - 'octal': Octal representation of file permissions (e.g., '0o644')
            - 'readable': Human-readable permission string (e.g., 'rw-r--r--')
            - 'owner_read': Boolean indicating if owner has read permission
            - 'owner_write': Boolean indicating if owner has write permission
            - 'owner_execute': Boolean indicating if owner has execute permission
            - 'group_read': Boolean indicating if group has read permission
            - 'group_write': Boolean indicating if group has write permission
            - 'group_execute': Boolean indicating if group has execute permission
            - 'others_read': Boolean indicating if others have read permission
            - 'others_write': Boolean indicating if others have write permission
            - 'others_execute': Boolean indicating if others have execute permission

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there's no permission to access the file.
    """
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Get file stats
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode

        # Convert to octal representation
        octal_permissions = oct(mode & 0o777)

        # Create readable permission string
        readable_permissions = stat.filemode(mode)

        # Detailed permission breakdown
        return {
            'octal': octal_permissions,
            'readable': readable_permissions,
            'owner_read': bool(mode & stat.S_IRUSR),
            'owner_write': bool(mode & stat.S_IWUSR),
            'owner_execute': bool(mode & stat.S_IXUSR),
            'group_read': bool(mode & stat.S_IRGRP),
            'group_write': bool(mode & stat.S_IWGRP),
            'group_execute': bool(mode & stat.S_IXGRP),
            'others_read': bool(mode & stat.S_IROTH),
            'others_write': bool(mode & stat.S_IWOTH),
            'others_execute': bool(mode & stat.S_IXOTH)
        }
    except PermissionError:
        raise PermissionError(f"No permission to access file: {file_path}")