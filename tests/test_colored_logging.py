import pytest
from termcolor import colored
from src.colored_logging import log_colored_message

def test_default_green_logging():
    """Test default green color logging."""
    result = log_colored_message("Test Message")
    assert result == colored("Test Message", 'green')

def test_different_colors():
    """Test logging with different supported colors."""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in colors:
        result = log_colored_message("Test Message", color=color)
        assert result == colored("Test Message", color)

def test_color_with_attributes():
    """Test logging with color and text attributes."""
    result = log_colored_message("Test Message", color='red', attrs=['bold', 'underline'])
    assert result == colored("Test Message", 'red', attrs=['bold', 'underline'])

def test_invalid_color_raises_error():
    """Test that an unsupported color raises a ValueError."""
    with pytest.raises(ValueError, match="Unsupported color. Choose from"):
        log_colored_message("Test Message", color='orange')

def test_non_string_message_raises_error():
    """Test that a non-string message raises a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_colored_message(123)

def test_empty_string_message():
    """Test logging an empty string."""
    result = log_colored_message("")
    assert result == colored("", 'green')

def test_whitespace_message():
    """Test logging a whitespace message."""
    result = log_colored_message("   ")
    assert result == colored("   ", 'green')