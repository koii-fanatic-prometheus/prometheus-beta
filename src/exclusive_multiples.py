def filter_exclusive_multiples(numbers):
    """
    Filter a list of integers to return numbers that are multiples of 3 or 5, but not both.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A sorted list of integers that are multiples of 3 or 5, but not both.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter numbers that are multiples of 3 or 5, but not both
    def is_exclusive_multiple(num):
        return (num % 3 == 0) != (num % 5 == 0)
    
    exclusive_multiples = list(filter(is_exclusive_multiple, numbers))
    
    # Return sorted list based on absolute value
    return sorted(exclusive_multiples, key=abs)