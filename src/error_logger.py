import logging
import functools
import traceback
import sys
import os

def ensure_log_file_directory(log_file):
    """
    Ensure the directory for the log file exists.
    
    Args:
        log_file (str): Path to the log file.
    """
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

def log_error(log_file='error.log', log_level=logging.ERROR):
    """
    A decorator that logs any exceptions raised by the decorated function.
    
    Args:
        log_file (str, optional): Path to the log file. Defaults to 'error.log'.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.
    
    Returns:
        Wrapper function that catches and logs any exceptions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Ensure log file directory exists
                ensure_log_file_directory(log_file)
                
                # Configure logging
                logging.basicConfig(
                    filename=log_file, 
                    level=log_level, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a'  # Append mode
                )
                
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
                logging.error(log_message)
                
                # Re-raise the exception to maintain original error handling
                raise
        return wrapper
    return decorator

def custom_error_log(message, log_file='error.log', log_level=logging.ERROR):
    """
    Log a custom error message to a specified log file.
    
    Args:
        message (str): Custom error message to log.
        log_file (str, optional): Path to the log file. Defaults to 'error.log'.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.
    """
    # Ensure log file directory exists
    ensure_log_file_directory(log_file)
    
    # Configure logging
    logging.basicConfig(
        filename=log_file, 
        level=log_level, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'  # Append mode
    )
    
    # Log the custom message
    logging.error(message)