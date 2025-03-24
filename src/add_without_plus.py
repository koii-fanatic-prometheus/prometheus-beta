def add_without_plus(a: int, b: int) -> int:
    """
    Implement addition of two integers without using the '+' operator.
    
    Uses bitwise operations to simulate addition:
    - XOR handles addition without carry
    - AND and left shift handle carry bits
    
    Args:
        a (int): First integer to add
        b (int): Second integer to add
    
    Returns:
        int: Sum of a and b
    
    Raises:
        TypeError: If inputs are not integers
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both arguments must be integers")
    
    # Handle edge case of zero
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Bitwise addition algorithm
    while b != 0:
        # Carry now contains common set bits of a and b
        carry = a & b
        
        # Sum of bits of a and b where at least one of the bits is not set
        a = a ^ b
        
        # Carry is shifted by one so that adding it to a gives the required sum
        b = carry << 1
    
    return a