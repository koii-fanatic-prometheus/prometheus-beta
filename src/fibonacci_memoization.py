def fibonacci_memoized(n):
    """
    Compute the nth Fibonacci number using memoization for efficient calculation.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based indexing).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> fibonacci_memoized(0)
        0
        >>> fibonacci_memoized(1)
        1
        >>> fibonacci_memoized(5)
        5
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Memoization using a list to store computed Fibonacci numbers
    memo = [0] * (n + 1)
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Initialize first two Fibonacci numbers
    memo[0] = 0
    memo[1] = 1
    
    # Compute subsequent Fibonacci numbers
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]