import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import ReadlineLogger

def test_readline_logger_initialization():
    """Test that ReadlineLogger can be initialized with default or custom logger."""
    # Default logger
    default_logger = ReadlineLogger()
    assert default_logger.logger is not None
    assert isinstance(default_logger.logger, logging.Logger)
    
    # Custom logger
    custom_logger = logging.getLogger('test_logger')
    custom_readline_logger = ReadlineLogger(custom_logger)
    assert custom_readline_logger.logger == custom_logger

def test_readline_logger_basic_input():
    """Test basic input logging."""
    # Redirect stdout to capture print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    with patch('builtins.input', return_value='test_input'):
        logger = ReadlineLogger()
        result = logger.log_input("Enter something: ")
        
        # Restore stdout
        sys.stdout = sys.__stdout__
    
    assert result == 'test_input'

def test_readline_logger_input_validation():
    """Test input validation functionality."""
    def validate_positive_int(s):
        """Validate that input is a positive integer."""
        try:
            return int(s) > 0
        except ValueError:
            return False
    
    # Simulate multiple inputs: first two invalid, third valid
    inputs = iter(['0', '-5', '10'])
    
    with patch('builtins.input', side_effect=inputs):
        logger = ReadlineLogger()
        result = logger.log_input(
            "Enter a positive number: ", 
            input_validator=validate_positive_int
        )
    
    assert result == '10'

def test_readline_logger_max_attempts():
    """Test max attempts limitation."""
    # Simulate repeated invalid inputs
    inputs = iter(['invalid']*4)
    
    def always_fail_validator(s):
        return False
    
    with patch('builtins.input', side_effect=inputs):
        logger = ReadlineLogger()
        result = logger.log_input(
            "Enter valid input: ", 
            input_validator=always_fail_validator, 
            max_attempts=3
        )
    
    assert result is None

def test_readline_logger_invalid_parameters():
    """Test error handling for invalid input parameters."""
    logger = ReadlineLogger()
    
    # Invalid prompt type
    with pytest.raises(TypeError):
        logger.log_input(123)
    
    # Invalid max attempts
    with pytest.raises(ValueError):
        logger.log_input("Prompt", max_attempts=0)

def test_readline_logger_keyboard_interrupt():
    """Test handling of keyboard interrupt."""
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        logger = ReadlineLogger()
        result = logger.log_input("Enter something: ")
    
    assert result is None