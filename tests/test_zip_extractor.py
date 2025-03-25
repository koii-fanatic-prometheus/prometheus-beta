import os
import zipfile
import pytest
import tempfile
import shutil

from src.zip_extractor import extract_zip_archive


def test_extract_zip_basic():
    """Test basic zip extraction functionality."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test.zip')
        with zipfile.ZipFile(zip_path, 'w') as zf:
            zf.writestr('file1.txt', 'content1')
            zf.writestr('file2.txt', 'content2')
        
        # Extract the zip
        extracted_files = extract_zip_archive(zip_path)
        
        # Verify extraction
        assert len(extracted_files) == 2
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)
        assert all(os.path.exists(f) for f in extracted_files)


def test_extract_zip_custom_path():
    """Test extracting zip to a custom directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test.zip')
        extract_dir = os.path.join(temp_dir, 'extracted')
        
        with zipfile.ZipFile(zip_path, 'w') as zf:
            zf.writestr('file.txt', 'content')
        
        # Extract the zip to a custom path
        extracted_files = extract_zip_archive(zip_path, extract_dir)
        
        # Verify extraction
        assert len(extracted_files) == 1
        assert extracted_files[0].startswith(extract_dir)
        assert os.path.exists(extracted_files[0])


def test_extract_zip_nonexistent_file():
    """Test extracting a non-existent zip file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_zip = os.path.join(temp_dir, 'nonexistent.zip')
        
        with pytest.raises(FileNotFoundError):
            extract_zip_archive(non_existent_zip)


def test_extract_zip_invalid_zip():
    """Test extracting an invalid zip file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        invalid_zip_path = os.path.join(temp_dir, 'invalid.zip')
        
        # Create a file that is not a valid zip
        with open(invalid_zip_path, 'w') as f:
            f.write('Not a zip file')
        
        with pytest.raises(ValueError):
            extract_zip_archive(invalid_zip_path)


def test_extract_zip_nested_files():
    """Test extracting zip with nested directory structure."""
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, 'nested.zip')
        
        with zipfile.ZipFile(zip_path, 'w') as zf:
            zf.writestr('dir1/dir2/file.txt', 'nested content')
        
        # Extract the zip
        extracted_files = extract_zip_archive(zip_path)
        
        # Verify extraction
        assert len(extracted_files) == 1
        assert 'dir1/dir2/file.txt' in extracted_files[0]
        assert os.path.exists(extracted_files[0])