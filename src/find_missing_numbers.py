def find_missing_numbers(arr):
    """
    Find and return all numbers that are missing from the given array of unique integers.
    
    Args:
        arr (list): A list of unique integers 
    
    Returns:
        list: A sorted list of missing numbers in the range of the input array
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input contains duplicate numbers
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for duplicates
    if len(arr) != len(set(arr)):
        raise ValueError("Input list must contain unique integers")
    
    # If array is empty, return empty list
    if not arr:
        return []
    
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Create a set of the input array for O(1) lookup
    arr_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_val, max_val + 1) 
        if num not in arr_set
    ]
    
    return sorted(missing_numbers)