def recursive_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using recursion.
    
    The function uses the Euclidean algorithm to find the GCD. 
    It recursively divides the larger number by the smaller number 
    and takes the remainder until the remainder is zero.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
        TypeError: If inputs are not integers
    """
    # Type checking
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Handle negative inputs
    a, b = abs(a), abs(b)
    
    # Base case: if b is zero, return a
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) = GCD(b, a % b)
    return recursive_gcd(b, a % b)