def fibonacci_memoized(n):
    """
    Calculate the nth Fibonacci number using recursion and memoization.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Memoization cache to store previously calculated Fibonacci numbers
    memo = {}
    
    def fib_helper(k):
        # Base cases
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Check if result is already memoized
        if k in memo:
            return memo[k]
        
        # Calculate and memoize the result
        memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]
    
    return fib_helper(n)