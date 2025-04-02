def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for efficient sorting.
    
    Flash Sort is a distribution sorting algorithm that works well for 
    various input distributions, with an average time complexity of O(n).
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list contains non-comparable elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Find min and max to calculate class range
    try:
        min_val = min(arr)
        max_val = max(arr)
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Special case: all elements are the same
    if min_val == max_val:
        return arr
    
    # Number of classes/buckets
    n = len(arr)
    m = max(int(0.42 * n), 2)  # Ensure at least 2 classes
    
    # Compute class distribution
    def get_class(x):
        return int(((x - min_val) / (max_val - min_val)) * (m - 1))
    
    # Initialize class weights
    weights = [0] * m
    
    # Count elements in each class
    for x in arr:
        j = get_class(x)
        weights[j] += 1
    
    # Compute cumulative weights
    for j in range(1, m):
        weights[j] += weights[j-1]
    
    # Buckets to hold sorted elements
    buckets = [[] for _ in range(m)]
    
    # Distribute elements into buckets
    for x in arr:
        j = get_class(x)
        buckets[j].append(x)
    
    # Sort each bucket
    for j in range(m):
        buckets[j].sort()
    
    # Reconstruct the array
    k = 0
    for bucket in buckets:
        for x in bucket:
            arr[k] = x
            k += 1
    
    return arr