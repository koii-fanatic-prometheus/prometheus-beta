import os
import pytest
import stat
from src.file_permissions import get_file_permissions

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file with specific permissions for testing."""
    test_file = tmp_path / "test_permissions.txt"
    test_file.write_text("Test file for permissions")
    test_file.chmod(0o644)  # rw-r--r--
    return str(test_file)

@pytest.fixture
def restricted_file(tmp_path):
    """Create a sample file with restrictive permissions."""
    test_file = tmp_path / "restricted_file.txt"
    test_file.write_text("Restricted file")
    test_file.chmod(0o600)  # rw-------
    return str(test_file)

def test_get_file_permissions_basic(sample_file):
    """Test basic file permissions retrieval."""
    permissions = get_file_permissions(sample_file)
    
    assert permissions['octal'] == '0o644'
    assert permissions['readable'] == '-rw-r--r--'
    
    # Owner permissions
    assert permissions['owner_read'] is True
    assert permissions['owner_write'] is True
    assert permissions['owner_execute'] is False
    
    # Group permissions
    assert permissions['group_read'] is True
    assert permissions['group_write'] is False
    assert permissions['group_execute'] is False
    
    # Others permissions
    assert permissions['others_read'] is True
    assert permissions['others_write'] is False
    assert permissions['others_execute'] is False

def test_get_file_permissions_restrictive(restricted_file):
    """Test file with more restrictive permissions."""
    permissions = get_file_permissions(restricted_file)
    
    assert permissions['octal'] == '0o600'
    assert permissions['readable'] == '-rw-------'
    
    # Only owner has permissions
    assert permissions['owner_read'] is True
    assert permissions['owner_write'] is True
    assert permissions['owner_execute'] is False
    
    assert permissions['group_read'] is False
    assert permissions['group_write'] is False
    assert permissions['group_execute'] is False
    
    assert permissions['others_read'] is False
    assert permissions['others_write'] is False
    assert permissions['others_execute'] is False

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_permissions("/path/to/nonexistent/file.txt")

# Additional test to verify executable file permissions
def test_executable_file(tmp_path):
    """Test file with execute permissions."""
    exec_file = tmp_path / "script.sh"
    exec_file.write_text("#!/bin/bash\necho 'Hello'")
    exec_file.chmod(0o755)  # rwxr-xr-x
    
    permissions = get_file_permissions(str(exec_file))
    
    assert permissions['octal'] == '0o755'
    assert permissions['readable'] == '-rwxr-xr-x'
    
    # Executable checks
    assert permissions['owner_execute'] is True
    assert permissions['group_execute'] is True
    assert permissions['others_execute'] is True