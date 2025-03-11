import os
import pytest
import tempfile
from src.file_exists import is_file_exists

def test_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test that the function returns True for an existing file
        assert is_file_exists(temp_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_non_existing_file():
    # Test that the function returns False for a non-existing file
    non_existent_path = "/path/to/definitely/non/existing/file.txt"
    assert is_file_exists(non_existent_path) is False

def test_directory():
    # Test that the function returns False for a directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Directories should return False
        assert is_file_exists(temp_dir) is False
    finally:
        # Clean up the temporary directory
        os.rmdir(temp_dir)

def test_invalid_input_type():
    # Test that the function raises TypeError for non-string inputs
    with pytest.raises(TypeError, match="File path must be a string"):
        is_file_exists(123)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        is_file_exists(None)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        is_file_exists(["file.txt"])