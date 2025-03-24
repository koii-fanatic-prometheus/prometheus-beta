import pytest
import logging
import time
from src.performance_logger import log_execution_time

# Create a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.INFO)

# Capture logs for testing
class LogCapture:
    def __init__(self, logger):
        self.logs = []
        self.handler = logging.Handler()
        self.handler.emit = lambda record: self.logs.append(record)
        logger.addHandler(self.handler)

    def get_logs(self):
        return [record.getMessage() for record in self.logs]

def test_log_execution_time_basic():
    """Test basic functionality of execution time logging"""
    log_capture = LogCapture(test_logger)
    
    @log_execution_time(logger=test_logger)
    def simple_function():
        time.sleep(0.1)  # Simulate some work
    
    simple_function()
    
    # Check that a log was created
    logs = log_capture.get_logs()
    assert len(logs) == 1
    assert "Function 'simple_function' executed in" in logs[0]
    assert float(logs[0].split()[-2]) >= 0.1

def test_log_execution_time_with_arguments():
    """Test logging with function that takes arguments"""
    log_capture = LogCapture(test_logger)
    
    @log_execution_time(logger=test_logger)
    def function_with_args(a, b):
        time.sleep(0.05)
        return a + b
    
    result = function_with_args(3, 4)
    assert result == 7
    
    logs = log_capture.get_logs()
    assert len(logs) == 1
    assert "Function 'function_with_args' executed in" in logs[0]

def test_log_execution_time_exception():
    """Test logging when an exception occurs"""
    log_capture = LogCapture(test_logger)
    
    @log_execution_time(logger=test_logger)
    def function_raising_error():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        function_raising_error()
    
    logs = log_capture.get_logs()
    assert len(logs) == 1
    assert "Error in function 'function_raising_error'" in logs[0]

def test_log_execution_time_no_logger():
    """Test that function works with default root logger"""
    @log_execution_time()
    def default_logger_function():
        time.sleep(0.05)
    
    # Should not raise any exceptions
    default_logger_function()