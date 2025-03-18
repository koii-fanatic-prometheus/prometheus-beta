import pytest
import time
import io
import sys
from src.execution_time_measurer import measure_execution_time

def test_measure_execution_time_basic():
    """Test basic functionality of measure_execution_time decorator"""
    @measure_execution_time
    def simple_function():
        time.sleep(0.1)
    
    # Capture stdout to check printed execution time
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    simple_function()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check output
    output = captured_output.getvalue().strip()
    assert "Execution time of simple_function:" in output
    assert output.endswith("seconds")

def test_measure_execution_time_with_args():
    """Test decorator with a function that takes arguments"""
    @measure_execution_time
    def add_numbers(a, b):
        time.sleep(0.05)
        return a + b
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    result = add_numbers(3, 4)
    
    sys.stdout = sys.__stdout__
    
    assert result == 7
    output = captured_output.getvalue().strip()
    assert "Execution time of add_numbers:" in output

def test_measure_execution_time_error_handling():
    """Test decorator's behavior with function that raises an exception"""
    @measure_execution_time
    def error_function():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        error_function()

def test_measure_execution_time_invalid_input():
    """Test the decorator with an invalid input"""
    with pytest.raises(TypeError):
        measure_execution_time(42)  # Not a callable