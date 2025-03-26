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
    
    # Comparison function that falls back to string representation
    def safe_compare(a, b):
        try:
            return a > b
        except TypeError:
            return str(a) > str(b)
    
    # Check first element
    if safe_compare(arr[0], arr[1]):
        local_maxima.append(0)
    
    # Check middle elements
    for i in range(1, len(arr) - 1):
        if (safe_compare(arr[i], arr[i-1]) and 
            safe_compare(arr[i], arr[i+1])):
            local_maxima.append(i)
    
    # Check last element
    if safe_compare(arr[-1], arr[-2]):
        local_maxima.append(len(arr) - 1)
    
    return local_maxima