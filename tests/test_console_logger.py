import pytest
import sys
from io import StringIO

from src.console_logger import log_message

def test_log_message_prints_correctly():
    """Test that the log_message function prints the message correctly."""
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Test logging a simple message
    test_message = "Hello, world!"
    log_message(test_message)

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check if the message was printed correctly
    assert captured_output.getvalue().strip() == test_message

def test_log_message_with_empty_string():
    """Test logging an empty string."""
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Test logging an empty string
    log_message("")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check if an empty string is printed correctly
    assert captured_output.getvalue().strip() == ""

def test_log_message_raises_type_error_for_non_string():
    """Test that TypeError is raised for non-string inputs."""
    # Test with various non-string types
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(42)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(None)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(["not", "a", "string"])