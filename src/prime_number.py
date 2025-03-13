def is_prime(number: int) -> bool:
    """
    Determine if a given number is prime.

    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Check for valid input
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    # Negative numbers, 0, and 1 are not prime
    if number < 2:
        return False
    
    # Check for divisibility up to the square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    
    return True