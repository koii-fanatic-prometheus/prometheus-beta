def find_array_xor(arr):
    """
    Calculate the XOR of all elements in the given array.

    Args:
        arr (list): A list of integers to perform XOR operation on.

    Returns:
        int: The result of XORing all elements in the array.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if len(arr) == 0:
        raise ValueError("Cannot calculate XOR of an empty list")
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Start with the first element
    result = arr[0]
    
    # XOR with subsequent elements
    for num in arr[1:]:
        result ^= num
    
    return result