def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers to process.
    
    Returns:
        int: Sum of unique elements in the array.
    
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
    # Handle empty array case
    if not arr:
        return 0
    
    # Use a set to track unique elements efficiently
    unique_elements = set()
    unique_sum = 0
    
    # Single pass through the array to track unique elements
    for num in arr:
        # If this is first occurrence, add to sum and tracking set
        if num not in unique_elements:
            unique_elements.add(num)
            unique_sum += num
        # If already seen before, remove from sum if it was previously counted
        elif num in unique_sum:
            unique_sum -= num
    
    return unique_sum