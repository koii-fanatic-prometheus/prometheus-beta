import os
import pytest
import tempfile
import shutil

from src.directory_exists import check_directory_exists

def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_directory_exists(temp_dir) is True

def test_nonexistent_directory():
    """Test that a nonexistent directory returns False."""
    # Create a path that is extremely unlikely to exist
    nonexistent_path = "/path/to/nonexistent/directory/that/should/not/exist"
    assert check_directory_exists(nonexistent_path) is False

def test_file_path_returns_false():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert check_directory_exists(temp_file.name) is False

def test_invalid_input_type():
    """Test that passing a non-string type raises a TypeError."""
    with pytest.raises(TypeError, match="Path must be a string"):
        check_directory_exists(123)
    with pytest.raises(TypeError, match="Path must be a string"):
        check_directory_exists(None)

def test_relative_path():
    """Test checking a relative directory path."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Change to temp directory
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)
            
            # Create a subdirectory
            os.mkdir('test_subdir')
            
            # Check relative path
            assert check_directory_exists('test_subdir') is True
            assert check_directory_exists('./test_subdir') is True
        finally:
            # Change back to original working directory
            os.chdir(original_cwd)

def test_path_with_spaces():
    """Test directory path with spaces."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a directory with spaces
        space_dir = os.path.join(temp_dir, 'directory with spaces')
        os.mkdir(space_dir)
        
        assert check_directory_exists(space_dir) is True