import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the sleep sort algorithm.
    
    Sleep sort works by creating a separate thread for each number in the input array,
    where each thread sleeps for a duration proportional to its number before adding 
    the number to the result list.
    
    Args:
        arr (List[Union[int, float]]): Input list of numbers to be sorted
    
    Returns:
        List[Union[int, float]]: Sorted list of numbers
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric values
        ValueError: If list contains negative numbers
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Check for negative numbers
    if any(x < 0 for x in arr):
        raise ValueError("Sleep sort does not work with negative numbers")
    
    # Empty list handling
    if not arr:
        return []
    
    # Synchronization primitives
    result = []
    lock = threading.Lock()
    
    def sort_thread(num):
        """Internal thread function for sorting a single number."""
        # Sleep proportional to the number's value
        time.sleep(num * 0.001)  # Scaled sleep to make sorting more reliable
        
        # Thread-safe append to result
        with lock:
            result.append(num)
    
    # Create and start threads
    threads = []
    for num in arr:
        t = threading.Thread(target=sort_thread, args=(num,))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    return result