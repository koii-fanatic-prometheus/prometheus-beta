import pytest
from src.recursive_string_reversal import recursive_reverse_string

def test_basic_string_reversal():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"
    assert recursive_reverse_string("world") == "dlrow"

def test_mixed_case_reversal():
    """Test reversal with mixed case"""
    assert recursive_reverse_string("Hello World") == "dlroW olleH"
    assert recursive_reverse_string("PyThOn") == "nOhTyP"

def test_single_character():
    """Test single character input"""
    assert recursive_reverse_string("a") == "a"
    assert recursive_reverse_string("Z") == "Z"

def test_empty_string():
    """Test empty string input"""
    assert recursive_reverse_string("") == ""

def test_only_spaces():
    """Test input with only spaces"""
    assert recursive_reverse_string(" ") == " "
    assert recursive_reverse_string("  ") == "  "

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        recursive_reverse_string(123)
    with pytest.raises(TypeError):
        recursive_reverse_string(None)
    with pytest.raises(TypeError):
        recursive_reverse_string([])

def test_invalid_characters():
    """Test input with invalid characters"""
    with pytest.raises(ValueError):
        recursive_reverse_string("Hello123")
    with pytest.raises(ValueError):
        recursive_reverse_string("Hello!")
    with pytest.raises(ValueError):
        recursive_reverse_string("Hi@")