import os
import pytest
import tempfile
from src.file_reader import read_text_file

def test_read_text_file_successful():
    """Test reading a text file successfully."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        test_content = "Hello, world!\nThis is a test file."
        temp_file.write(test_content)
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == test_content
        finally:
            os.unlink(temp_file.name)

def test_read_text_file_empty():
    """Test reading an empty text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("")
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == ""
        finally:
            os.unlink(temp_file.name)

def test_read_text_file_not_found():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        read_text_file('non_existent_file.txt')

def test_read_text_file_with_unicode():
    """Test reading a file with Unicode characters."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        unicode_content = "Hello, 世界! こんにちは"
        temp_file.write(unicode_content)
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == unicode_content
        finally:
            os.unlink(temp_file.name)