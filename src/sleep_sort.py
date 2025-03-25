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
    
    # Find max value to scale sleep times appropriately
    max_val = max(arr)
    
    # Synchronization primitives
    result = []
    lock = threading.Lock()
    finished_event = threading.Event()
    
    def sort_thread(num, index):
        """Internal thread function for sorting a single number."""
        # Normalize sleep time to be proportional but consistent
        scaled_num = num / (max_val + 1)
        base_sleep = 0.01  # Consistent base sleep time
        sleep_time = scaled_num * base_sleep
        time.sleep(sleep_time)
        
        # Thread-safe append to result
        with lock:
            result.append((index, num))
            
            # If this is the last thread, set the finished event
            if len(result) == len(arr):
                finished_event.set()
    
    # Create and start threads
    threads = []
    for index, num in enumerate(arr):
        t = threading.Thread(target=sort_thread, args=(num, index))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete (with timeout)
    finished_event.wait(timeout=1.0)
    
    # Sort based on original indices to maintain stable sort
    return [x[1] for x in sorted(result, key=lambda r: r[0])]