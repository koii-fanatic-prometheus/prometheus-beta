import os
import pytest
import tempfile
import shutil

from src.directory_utils import delete_empty_directory

def test_delete_empty_directory():
    """Test successfully deleting an empty directory."""
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create an additional empty directory inside
        empty_dir = os.path.join(temp_dir, 'empty_subdir')
        os.mkdir(empty_dir)
        
        # Attempt to delete the empty directory
        result = delete_empty_directory(empty_dir)
        
        # Verify directory is deleted
        assert result is True
        assert not os.path.exists(empty_dir)

def test_delete_nonexistent_directory():
    """Test attempting to delete a non-existent directory."""
    with pytest.raises(FileNotFoundError):
        delete_empty_directory('/path/to/nonexistent/directory')

def test_delete_nonempty_directory():
    """Test attempting to delete a non-empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a non-empty directory
        nonempty_dir = os.path.join(temp_dir, 'nonempty_dir')
        os.mkdir(nonempty_dir)
        
        # Create a file inside the directory
        with open(os.path.join(nonempty_dir, 'file.txt'), 'w') as f:
            f.write('content')
        
        # Attempt to delete the non-empty directory
        with pytest.raises(OSError):
            delete_empty_directory(nonempty_dir)

def test_delete_file_instead_of_directory():
    """Test attempting to delete a file instead of a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary file
        file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('content')
        
        # Attempt to delete the file as if it were a directory
        with pytest.raises(ValueError):
            delete_empty_directory(file_path)