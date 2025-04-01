import math

def is_perfect_square(number):
    """
    Check if a given number is a perfect square.

    A perfect square is a number that can be expressed as the product of an integer with itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a perfect square, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Validate input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Negative numbers cannot be perfect squares
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0 and 1
    if number in [0, 1]:
        return True
    
    # Use integer square root method
    # A number is a perfect square if its square root is an integer
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number