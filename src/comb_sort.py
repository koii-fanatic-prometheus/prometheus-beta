def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list.
    
    Comb Sort is an improvement over Bubble Sort. It eliminates turtles, 
    or small values near the end of the list, by using a gap size that 
    starts large and reduces over iterations.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Initial gap, typically the list length divided by 1.3
    gap = len(arr)
    shrink = 1.3  # Empirically determined shrink factor
    sorted_flag = False
    
    while not sorted_flag:
        # Update gap
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True  # Last pass
        
        # Compare elements with current gap
        for i in range(len(arr) - gap):
            # Compare and swap if needed
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
    
    return arr