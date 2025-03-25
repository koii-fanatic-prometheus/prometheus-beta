import pytest
from src.string_case_converter import convert_to_lowercase_with_spaces

def test_convert_to_lowercase_with_spaces():
    """Test basic lowercase conversion."""
    assert convert_to_lowercase_with_spaces("Hello World") == "hello world"

def test_already_lowercase():
    """Test string that is already lowercase."""
    assert convert_to_lowercase_with_spaces("hello world") == "hello world"

def test_mixed_case_with_spaces():
    """Test mixed case string with various spaces."""
    assert convert_to_lowercase_with_spaces("HeLLo   WoRLD") == "hello   world"

def test_empty_string():
    """Test empty string input."""
    assert convert_to_lowercase_with_spaces("") == ""

def test_string_with_numbers_and_symbols():
    """Test string with numbers and symbols."""
    assert convert_to_lowercase_with_spaces("Hello123 World!") == "hello123 world!"

def test_invalid_input_type():
    """Test handling of non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(None)