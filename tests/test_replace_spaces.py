import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_replace_spaces_normal_string():
    """Test replacing spaces in a normal string."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_multiple_spaces():
    """Test replacing multiple consecutive spaces."""
    assert replace_spaces_with_underscores("  multiple   spaces  ") == "__multiple___spaces__"

def test_replace_spaces_empty_string():
    """Test handling of an empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_no_spaces():
    """Test a string with no spaces."""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_none_input():
    """Test handling of None input."""
    with pytest.raises(ValueError, match="Input string cannot be None"):
        replace_spaces_with_underscores(None)