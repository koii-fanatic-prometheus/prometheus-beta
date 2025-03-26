def find_local_maxima(arr):
    """
    Find local maximum values in an input array.
    
    A local maximum is an element that is strictly greater than its immediate neighbors.
    For the first and last elements, they are local maxima if they are strictly greater 
    than their single adjacent neighbor.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Indices of local maximum values in the input array
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element array case
    if len(arr) == 1:
        return [0]
    
    local_maxima = []
    
    # Check first element
    try:
        if arr[0] > arr[1]:
            local_maxima.append(0)
    except TypeError:
        # If comparison fails, try comparing their string representations
        if str(arr[0]) > str(arr[1]):
            local_maxima.append(0)
    
    # Check middle elements
    for i in range(1, len(arr) - 1):
        try:
            # Check if current element is strictly greater than both neighbors
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                local_maxima.append(i)
        except TypeError:
            # If direct comparison fails, use string representation
            if (str(arr[i]) > str(arr[i-1]) and 
                str(arr[i]) > str(arr[i+1])):
                local_maxima.append(i)
    
    # Check last element
    try:
        if arr[-1] > arr[-2]:
            local_maxima.append(len(arr) - 1)
    except TypeError:
        # If comparison fails, try comparing string representations
        if str(arr[-1]) > str(arr[-2]):
            local_maxima.append(len(arr) - 1)
    
    return local_maxima