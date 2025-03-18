import os
import pytest
import shutil
from src.file_backup import create_file_backup

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing."""
    sample_content = "This is a test file for backup."
    file_path = tmp_path / "test_file.txt"
    file_path.write_text(sample_content)
    return str(file_path)

def test_backup_creates_file_in_same_directory(sample_file):
    """Test that backup creates a file in the same directory."""
    backup_path = create_file_backup(sample_file)
    
    assert os.path.exists(backup_path)
    assert os.path.dirname(backup_path) == os.path.dirname(sample_file)
    assert os.path.basename(sample_file) in os.path.basename(backup_path)

def test_backup_creates_file_in_specified_directory(sample_file, tmp_path):
    """Test backing up to a specified directory."""
    backup_dir = tmp_path / "backups"
    backup_path = create_file_backup(sample_file, str(backup_dir))
    
    assert os.path.exists(backup_path)
    assert os.path.dirname(backup_path) == str(backup_dir)

def test_backup_preserves_file_content(sample_file):
    """Test that the backup preserves original file content."""
    original_content = open(sample_file, 'r').read()
    backup_path = create_file_backup(sample_file)
    
    backup_content = open(backup_path, 'r').read()
    assert original_content == backup_content

def test_backup_fails_on_nonexistent_file():
    """Test that backing up a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        create_file_backup("/path/to/nonexistent/file.txt")

def test_backup_fails_on_directory():
    """Test that attempting to backup a directory raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        create_file_backup(os.path.dirname(os.path.abspath(__file__)))

def test_backup_filename_includes_timestamp(sample_file):
    """Test that backup filename includes a timestamp."""
    backup_path = create_file_backup(sample_file)
    
    base_filename = os.path.basename(sample_file)
    backup_filename = os.path.basename(backup_path)
    
    assert base_filename in backup_filename
    assert backup_filename != base_filename  # Timestamp makes it unique