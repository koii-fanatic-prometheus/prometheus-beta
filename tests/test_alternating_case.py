import pytest
from src.alternating_case import to_alternating_constant_case

def test_alternating_case_basic():
    """Test basic string conversion"""
    assert to_alternating_constant_case("hello") == "HeLlO"
    assert to_alternating_constant_case("python") == "PyThOn"

def test_alternating_case_empty_string():
    """Test empty string input"""
    assert to_alternating_constant_case("") == ""

def test_alternating_case_single_char():
    """Test single character input"""
    assert to_alternating_constant_case("a") == "A"
    assert to_alternating_constant_case("B") == "B"

def test_alternating_case_multi_word():
    """Test multi-word string"""
    assert to_alternating_constant_case("hello world") == "HeLlO WoRlD"

def test_alternating_case_mixed_case():
    """Test string with mixed initial case"""
    assert to_alternating_constant_case("HeLLo") == "HeLlO"

def test_alternating_case_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        to_alternating_constant_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_constant_case(None)