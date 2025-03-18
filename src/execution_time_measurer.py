import time
from functools import wraps
from typing import Callable, Any

def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and prints the execution time of a function.

    Args:
        func (Callable): The function whose execution time is to be measured.

    Returns:
        Callable: A wrapped function that measures and prints execution time.
    
    Raises:
        TypeError: If the input is not a callable function.
    """
    # Check if the input is callable before proceeding
    if not callable(func):
        raise TypeError("Input must be a callable function")
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Record start time
        start_time = time.perf_counter()
        
        try:
            # Execute the function
            result = func(*args, **kwargs)
        except Exception as e:
            # Re-raise any exceptions from the original function
            raise e
        finally:
            # Calculate and print execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        
        return result
    
    return wrapper