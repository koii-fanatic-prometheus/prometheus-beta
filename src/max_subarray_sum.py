def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a one-dimensional array of integers.
    
    This function uses Kadane's algorithm to efficiently find the maximum subarray sum.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum subarray sum. 
        
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_ending_here = max_so_far = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Decide whether to start a new subarray or extend the existing one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum sum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far