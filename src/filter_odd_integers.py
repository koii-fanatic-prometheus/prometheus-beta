def filter_and_sort_odd_integers(numbers):
    """
    Filter out odd integers from the given list and return them sorted in ascending order.

    Args:
        numbers (list): A list of integers to be filtered and sorted.

    Returns:
        list: A new list containing only the odd integers from the input list, 
              sorted in ascending order.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.

    Examples:
        >>> filter_and_sort_odd_integers([1, 2, 3, 4, 5, 6, 7, 8, 9])
        [1, 3, 5, 7, 9]
        >>> filter_and_sort_odd_integers([2, 4, 6, 8])
        []
        >>> filter_and_sort_odd_integers([])
        []
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter out odd integers and sort
    return sorted([num for num in numbers if num % 2 != 0])