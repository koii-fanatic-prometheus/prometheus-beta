import pytest
from src.capitalize_words import capitalize_words

def test_basic_capitalization():
    """Test basic word capitalization."""
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"

def test_already_capitalized():
    """Test string with already capitalized words."""
    assert capitalize_words("Hello World") == "Hello World"

def test_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_single_word():
    """Test single word capitalization."""
    assert capitalize_words("hello") == "Hello"

def test_multiple_spaces():
    """Test string with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_mixed_case():
    """Test string with mixed case."""
    assert capitalize_words("hELLo wORLd") == "Hello World"

def test_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        capitalize_words(123)
    with pytest.raises(TypeError):
        capitalize_words(None)

def test_unicode_characters():
    """Test capitalization with unicode characters."""
    assert capitalize_words("äpfel sind gut") == "Äpfel Sind Gut"