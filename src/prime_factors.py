def find_prime_factors(n):
    """
    Find all prime factors of a positive integer in ascending order.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A sorted list of prime factors.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring while divisor squared is less than or equal to n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add to factors and divide n
            factors.append(divisor)
            n //= divisor
        else:
            # If not divisible, move to next potential divisor
            divisor += 1
    
    # If n is greater than 1, it is a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors