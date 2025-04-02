def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers to process.
    
    Returns:
        int: Sum of unique elements in the array.
    
    Raises:
        TypeError: If input contains non-integer elements.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> sum_unique_elements([1, 2, 3, 2])
        4
        >>> sum_unique_elements([1, 1, 1, 1])
        1
        >>> sum_unique_elements([])
        0
    """
    # Validate input type
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Handle empty array case
    if not arr:
        return 0
    
    # Use a set to track unique elements efficiently
    unique_elements = set()
    seen_multiple_times = set()
    unique_sum = 0
    
    # Single pass through the array to track unique elements
    for num in arr:
        # If first occurrence, add to sum and tracking set
        if num not in unique_elements:
            unique_elements.add(num)
            unique_sum += num
        # If seen before, remove from unique sum if not already tracked
        elif num not in seen_multiple_times:
            unique_sum -= num
            seen_multiple_times.add(num)
    
    return unique_sum