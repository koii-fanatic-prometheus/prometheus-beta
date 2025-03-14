def remove_duplicates(arr):
    """
    Remove duplicate elements from an array of integers while maintaining 
    the original order of first occurrence.

    Args:
        arr (list): Input list of integers

    Returns:
        list: A new list with duplicates removed, preserving the order 
              of first occurrence

    Time Complexity: O(n)
    Space Complexity: O(n)

    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([1, 1, 1, 1])
        [1]
    """
    # Use a set to track seen elements for O(1) lookup
    seen = set()
    # Use a list to preserve order of first occurrence
    result = []
    
    for num in arr:
        # Only add to result if not seen before
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result