def calculate_triangular_number(n):
    """
    Calculate the nth triangular number.
    
    A triangular number is the sum of the first n positive integers.
    For example, the 4th triangular number is 1 + 2 + 3 + 4 = 10.
    
    Args:
        n (int): The position of the triangular number to calculate.
    
    Returns:
        int: The nth triangular number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Check for invalid input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Triangular number can be calculated using the formula n * (n + 1) // 2
    return n * (n + 1) // 2