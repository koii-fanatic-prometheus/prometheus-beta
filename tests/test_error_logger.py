import os
import logging
import pytest
from src.error_logger import log_error, custom_error_log

def test_log_error_decorator():
    # Test log_error decorator
    log_file = 'test_decorator_error.log'
    
    @log_error(log_file=log_file)
    def error_function():
        raise ValueError("Test error")
    
    # Remove log file if it exists
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Expect the function to raise the original exception
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check if log file was created
    assert os.path.exists(log_file), "Log file was not created"
    
    # Read log file and verify contents
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert "Error in function 'error_function'" in log_content
    assert "ValueError - Test error" in log_content

def test_custom_error_log():
    # Test custom_error_log function
    log_file = 'test_custom_error.log'
    custom_message = "This is a custom error message"
    
    # Remove log file if it exists
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Log custom error
    custom_error_log(custom_message, log_file=log_file)
    
    # Check if log file was created
    assert os.path.exists(log_file), "Log file was not created"
    
    # Read log file and verify contents
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert custom_message in log_content

def test_default_log_file():
    # Test that default log file works
    default_log_file = 'error.log'
    
    # Remove default log file if it exists
    if os.path.exists(default_log_file):
        os.remove(default_log_file)
    
    custom_error_log("Default log file test")
    
    # Check if default log file was created
    assert os.path.exists(default_log_file), "Default log file was not created"

def test_log_error_decorator_preserves_function_metadata():
    @log_error()
    def sample_function(x, y):
        """This is a sample function."""
        return x + y
    
    assert sample_function.__name__ == 'sample_function'
    assert sample_function.__doc__ == "This is a sample function."