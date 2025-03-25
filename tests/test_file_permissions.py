import os
import pytest
import stat
from src.file_permissions import change_file_permissions

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing permissions."""
    test_file = tmp_path / "test_permissions.txt"
    test_file.write_text("Test file for permissions")
    return str(test_file)

def test_change_permissions_valid(temp_file):
    """Test changing file permissions to a valid value."""
    # Initially, let's check the current permissions
    initial_mode = os.stat(temp_file).st_mode
    
    # Change permissions to read-only for all
    change_file_permissions(temp_file, 0o444)
    
    # Get new permissions
    new_mode = os.stat(temp_file).st_mode
    
    # Check permissions changed correctly
    assert not bool(new_mode & stat.S_IWUSR)
    assert not bool(new_mode & stat.S_IWGRP)
    assert not bool(new_mode & stat.S_IWOTH)

def test_change_permissions_all_access(temp_file):
    """Test changing file permissions to full access."""
    change_file_permissions(temp_file, 0o777)
    
    # Get new permissions
    new_mode = os.stat(temp_file).st_mode
    
    # Check all permission bits are set
    assert bool(new_mode & stat.S_IRWXU)
    assert bool(new_mode & stat.S_IRWXG)
    assert bool(new_mode & stat.S_IRWXO)

def test_invalid_file_path():
    """Test changing permissions for a non-existent file."""
    with pytest.raises(FileNotFoundError):
        change_file_permissions("/path/to/nonexistent/file.txt", 0o755)

def test_invalid_permissions_type():
    """Test passing invalid permission types."""
    with pytest.raises(TypeError):
        change_file_permissions("some_file.txt", "755")
    
    with pytest.raises(TypeError):
        change_file_permissions("some_file.txt", 755.0)

def test_invalid_permissions_format(temp_file):
    """Test passing invalid permissions format."""
    with pytest.raises(ValueError):
        change_file_permissions(temp_file, 999)  # Invalid octal

def test_input_validation():
    """Test input type validation."""
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o755)
    
    with pytest.raises(TypeError):
        change_file_permissions(None, 0o755)