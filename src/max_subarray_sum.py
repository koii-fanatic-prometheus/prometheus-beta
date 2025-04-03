def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This implementation uses Kadane's algorithm to find the maximum subarray sum 
    in O(n) time complexity.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is empty
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        # Choose between extending current subarray or starting a new subarray
        current_sum = max(num, current_sum + num)
        # Update max sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum