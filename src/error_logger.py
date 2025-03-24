import logging
import functools
import traceback
import sys
import os
from datetime import datetime

def log_to_file(log_file, log_message, log_level=logging.ERROR):
    """
    Directly write a log message to a file.
    
    Args:
        log_file (str): Path to the log file.
        log_message (str): Message to log.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.
    """
    # Ensure log file directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create log message with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_log_message = f"{timestamp} - ERROR - {log_message}\n"
    
    # Write to file
    with open(log_file, 'a') as f:
        f.write(full_log_message)

def log_error(log_file='error.log'):
    """
    A decorator that logs any exceptions raised by the decorated function.
    
    Args:
        log_file (str, optional): Path to the log file. Defaults to 'error.log'.
    
    Returns:
        Wrapper function that catches and logs any exceptions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Get detailed error information
                error_type = type(e).__name__
                error_message = str(e)
                error_traceback = traceback.format_exc()
                
                # Construct a comprehensive error log message
                log_message = (
                    f"Error in function '{func.__name__}': "
                    f"{error_type} - {error_message}\n"
                    f"Traceback:\n{error_traceback}"
                )
                
                # Log the error
                log_to_file(log_file, log_message)
                
                # Re-raise the exception to maintain original error handling
                raise
        return wrapper
    return decorator

def custom_error_log(message, log_file='error.log'):
    """
    Log a custom error message to a specified log file.
    
    Args:
        message (str): Custom error message to log.
        log_file (str, optional): Path to the log file. Defaults to 'error.log'.
    """
    # Log the custom message
    log_to_file(log_file, message)