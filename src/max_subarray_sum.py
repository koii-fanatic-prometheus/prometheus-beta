def max_subarray_sum(arr):
    """
    Find the contiguous subarray with the largest sum in an array of integers.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        list: The contiguous subarray with the largest sum.
              If the input array is empty, returns an empty list.
    
    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        [4, -1, 2, 1]
        >>> max_subarray_sum([1])
        [1]
        >>> max_subarray_sum([])
        []
    """
    # Handle empty array case
    if not arr:
        return []
    
    # Handle single element array case
    if len(arr) == 1:
        return arr
    
    # Kadane's algorithm to find max subarray sum
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    max_start = 0
    max_end = 0
    
    for end, num in enumerate(arr):
        # If current_sum becomes negative, reset it and start a new subarray
        if current_sum < 0:
            current_sum = num
            start = end
        else:
            current_sum += num
        
        # Update max_sum and max subarray indices if current_sum is larger
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = end
    
    # Return the subarray with the largest sum
    return arr[max_start:max_end+1]