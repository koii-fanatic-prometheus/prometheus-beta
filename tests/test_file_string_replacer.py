"""
Test module for file_string_replacer function.

This module contains comprehensive tests for the string replacement functionality.
"""

import os
import pytest
from src.file_string_replacer import replace_string_in_file


@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Hello world! Hello universe! Hello everyone!")
    return str(file_path)


def test_successful_replacement(sample_file):
    """Test successful string replacement."""
    replacements = replace_string_in_file(sample_file, "Hello", "Hi")
    
    assert replacements == 3
    with open(sample_file, 'r') as file:
        content = file.read()
    assert content == "Hi world! Hi universe! Hi everyone!"


def test_no_replacements(sample_file):
    """Test when no replacements are made."""
    replacements = replace_string_in_file(sample_file, "Goodbye", "Hello")
    
    assert replacements == 0
    with open(sample_file, 'r') as file:
        content = file.read()
    assert content == "Hello world! Hello universe! Hello everyone!"


def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("nonexistent_file.txt", "old", "new")


def test_empty_old_string(sample_file):
    """Test handling of empty old string."""
    with pytest.raises(ValueError):
        replace_string_in_file(sample_file, "", "new")


def test_input_type_errors(sample_file):
    """Test type checking for function arguments."""
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file(sample_file, 123, "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file(sample_file, "old", 123)


def test_preserves_file_content(sample_file):
    """Ensure file content is preserved when no replacements are possible."""
    original_content = open(sample_file, 'r').read()
    replace_string_in_file(sample_file, "Nonexistent", "Replacement")
    
    with open(sample_file, 'r') as file:
        assert file.read() == original_content