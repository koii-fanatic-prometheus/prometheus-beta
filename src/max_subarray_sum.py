def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This function uses Kadane's algorithm to efficiently find the maximum subarray sum,
    handling both positive and negative numbers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list is empty
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far