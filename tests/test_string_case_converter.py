import pytest
from src.string_case_converter import to_kebab_case

def test_to_kebab_case_basic_conversions():
    """Test basic string conversions to kebab-case."""
    assert to_kebab_case("HelloWorld") == "hello-world"
    assert to_kebab_case("hello_world") == "hello-world"
    assert to_kebab_case("Hello World") == "hello-world"
    assert to_kebab_case("helloWorld") == "hello-world"

def test_to_kebab_case_edge_cases():
    """Test edge cases for kebab-case conversion."""
    assert to_kebab_case("") == ""
    assert to_kebab_case("a") == "a"
    assert to_kebab_case("A") == "a"
    assert to_kebab_case("123") == "123"

def test_to_kebab_case_mixed_inputs():
    """Test conversion of strings with mixed characters."""
    assert to_kebab_case("Hello_World Test") == "hello-world-test"
    assert to_kebab_case("hello-world_test") == "hello-world-test"
    assert to_kebab_case("HelloWorld123Test") == "hello-world-123-test"

def test_to_kebab_case_special_characters():
    """Test handling of special characters."""
    assert to_kebab_case("Hello@World") == "hello-world"
    assert to_kebab_case("hello world!") == "hello-world"
    assert to_kebab_case("  Hello  World  ") == "hello-world"

def test_to_kebab_case_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_kebab_case(None)
    with pytest.raises(TypeError):
        to_kebab_case(123)
    with pytest.raises(TypeError):
        to_kebab_case(["hello", "world"])