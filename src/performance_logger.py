import time
import functools
import logging

def log_execution_time(logger=None):
    """
    A decorator to log the execution time of a function.
    
    Args:
        logger (logging.Logger, optional): Logger to use for output. 
                If None, uses the root logger.
    
    Returns:
        callable: Decorated function that logs its execution time
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Select logger (use root logger if none provided)
            log = logger or logging.getLogger()
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log execution time
                log.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                log.error(f"Error in function '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    
    return decorator