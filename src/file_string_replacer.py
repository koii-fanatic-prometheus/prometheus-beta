"""
Module for replacing strings in files.

This module provides a function to replace all occurrences of a given string
in a file with another string, with error handling and flexibility.
"""

import os


def replace_string_in_file(file_path: str, old_string: str, new_string: str) -> int:
    """
    Replace all occurrences of a string in a file.

    Args:
        file_path (str): Path to the file to modify
        old_string (str): String to be replaced
        new_string (str): String to replace with

    Returns:
        int: Number of replacements made

    Raises:
        FileNotFoundError: If the specified file does not exist
        TypeError: If any input is not a string
        ValueError: If old_string is empty
    """
    # Input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(old_string, str):
        raise TypeError("old_string must be a string")
    if not isinstance(new_string, str):
        raise TypeError("new_string must be a string")
    
    if not old_string:
        raise ValueError("old_string cannot be empty")
    
    # Check file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Read file contents
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Count replacements and perform replacement
    replacements = content.count(old_string)
    modified_content = content.replace(old_string, new_string)
    
    # Write modified content back to file
    with open(file_path, 'w') as file:
        file.write(modified_content)
    
    return replacements