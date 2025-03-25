import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string conversion to alternating camel case."""
    assert to_alternating_camel_case("hello world") == "helloWorld"

def test_multiple_words():
    """Test conversion with multiple words."""
    assert to_alternating_camel_case("python is awesome") == "pythonIsAwesome"

def test_mixed_case_input():
    """Test input with mixed case words."""
    assert to_alternating_camel_case("PYTHON is AWESOME") == "pythonIsAwesome"

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_camel_case("hello") == "hello"

def test_multiple_spaces():
    """Test input with multiple spaces between words."""
    assert to_alternating_camel_case("  hello   world  ") == "helloWorld"

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_alternating_camel_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_camel_case(None)

def test_empty_input():
    """Test error handling for empty string inputs."""
    with pytest.raises(ValueError):
        to_alternating_camel_case("")
    
    with pytest.raises(ValueError):
        to_alternating_camel_case("   ")

def test_alternating_capitalization():
    """Test alternating capitalization with multiple words."""
    assert to_alternating_camel_case("one TWO three FOUR") == "oneTwoThreeFour"