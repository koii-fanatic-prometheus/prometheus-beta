import pytest
from src.inverse_case import convert_to_inverse_case

def test_basic_inverse_case():
    """Test basic string conversion to inverse case."""
    assert convert_to_inverse_case("Hello World!") == "hELLO wORLD!"
    assert convert_to_inverse_case("Python") == "pYTHON"
    assert convert_to_inverse_case("UPPER lower") == "upper LOWER"

def test_mixed_characters():
    """Test conversion with mixed alphanumeric and special characters."""
    assert convert_to_inverse_case("Hello 123 World!") == "hELLO 123 wORLD!"
    assert convert_to_inverse_case("Python 3.9") == "pYTHON 3.9"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_inverse_case("") == ""

def test_non_alphabetic_characters():
    """Test strings with only non-alphabetic characters."""
    assert convert_to_inverse_case("123!@#") == "123!@#"

def test_unicode_characters():
    """Test conversion with Unicode characters."""
    assert convert_to_inverse_case("Héllö Wörld") == "hÉLLÖ wÖRLD"

def test_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(["Hello"])