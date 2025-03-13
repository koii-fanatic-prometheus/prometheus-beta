def sum_even_indexed_elements(numbers):
    """
    Calculate the sum of elements at even indices in a given list of integers.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: Sum of elements at even indices (0, 2, 4, ...).
             Returns 0 if the list is empty.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.

    Examples:
        >>> sum_even_indexed_elements([1, 2, 3, 4, 5])
        9
        >>> sum_even_indexed_elements([-1, 2, -3, 4, -5])
        -4
        >>> sum_even_indexed_elements([])
        0
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if any(not isinstance(x, (int, bool)) for x in numbers):
        raise TypeError("All list elements must be integers")
    
    # Handle empty list case
    if not numbers:
        return 0
    
    # Sum elements at even indices (0, 2, 4, ...)
    return sum(numbers[::2])