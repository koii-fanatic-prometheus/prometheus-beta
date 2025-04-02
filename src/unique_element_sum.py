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
    
    # Use a dictionary to track element frequencies
    element_counts = {}
    
    # Count occurrences of each element
    for num in arr:
        element_counts[num] = element_counts.get(num, 0) + 1
    
    # Sum unique elements (those appearing only once)
    return sum(num for num, count in element_counts.items() if count == 1)