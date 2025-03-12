def has_common_element(arr1, arr2):
    """
    Check if two arrays have at least one common element.
    
    Args:
        arr1 (list): First input array
        arr2 (list): Second input array
    
    Returns:
        bool: True if arrays have a common element, False otherwise
    
    Time Complexity: O(n), where n is the total number of elements in both arrays
    Space Complexity: O(n) to store unique elements in a set
    
    Examples:
        >>> has_common_element([1, 2, 3], [4, 5, 6])
        False
        >>> has_common_element([1, 2, 3], [3, 4, 5])
        True
        >>> has_common_element([], [])
        False
    """
    # Handle edge cases of empty arrays
    if not arr1 or not arr2:
        return False
    
    # Convert first array to a set for O(1) lookup
    arr1_set = set(arr1)
    
    # Check for common elements with strict type comparison
    for item in arr2:
        if item in arr1_set:
            return True
    
    return False