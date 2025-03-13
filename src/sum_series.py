def sum_series(n: int) -> int:
    """
    Calculate the sum of all integers from 1 to n in constant time.
    
    This function uses the mathematical formula n * (n + 1) / 2 to 
    efficiently compute the sum of consecutive integers from 1 to n.
    
    Args:
        n (int): The upper limit of the series to sum.
    
    Returns:
        int: The sum of all integers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    
    Examples:
        >>> sum_series(5)  # 1 + 2 + 3 + 4 + 5 = 15
        15
        >>> sum_series(0)
        0
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use constant time formula to calculate sum
    return n * (n + 1) // 2