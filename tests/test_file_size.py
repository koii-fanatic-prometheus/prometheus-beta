import os
import pytest
import tempfile

from src.file_size import get_file_size

def test_get_file_size_normal():
    """Test getting size of a normal file"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file.close()
        
        try:
            file_size = get_file_size(temp_file.name)
            assert file_size == 13  # Length of "Hello, World!"
        finally:
            os.unlink(temp_file.name)

def test_get_file_size_empty_file():
    """Test getting size of an empty file"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()
        
        try:
            file_size = get_file_size(temp_file.name)
            assert file_size == 0
        finally:
            os.unlink(temp_file.name)

def test_get_file_size_large_file():
    """Test getting size of a larger file"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"A" * 1024 * 1024)  # 1MB file
        temp_file.close()
        
        try:
            file_size = get_file_size(temp_file.name)
            assert file_size == 1024 * 1024
        finally:
            os.unlink(temp_file.name)

def test_get_file_size_non_existent_file():
    """Test getting size of a non-existent file"""
    with pytest.raises(FileNotFoundError):
        get_file_size("non_existent_file.txt")

def test_get_file_size_directory():
    """Test attempting to get size of a directory"""
    with pytest.raises(IsADirectoryError):
        get_file_size(".")

def test_get_file_size_invalid_input():
    """Test providing an invalid input type"""
    with pytest.raises(TypeError):
        get_file_size(123)  # Passing an integer instead of a string