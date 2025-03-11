def cocktail_shaker_sort(arr):
    """
    Implement the cocktail shaker sort (bidirectional bubble sort) algorithm.
    
    This sorting algorithm is a variation of bubble sort that sorts in both 
    directions. It works by first moving the largest elements to the end of 
    the list, then moving the smallest elements to the beginning.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains elements that cannot be compared.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    arr = list(arr)
    
    # If list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Flag to track if any swaps occurred
    swapped = True
    start = 0
    end = len(arr) - 1
    
    while swapped:
        # Reset swapped flag
        swapped = False
        
        # Forward pass (left to right)
        for i in range(start, end):
            try:
                if arr[i] > arr[i + 1]:
                    # Swap elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
        
        # If no swapping occurred, list is sorted
        if not swapped:
            break
        
        # Decrease end index as the largest element is now at the end
        end -= 1
        
        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            try:
                if arr[i] > arr[i + 1]:
                    # Swap elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
        
        # Increase start index as the smallest element is now at the beginning
        start += 1
    
    return arr