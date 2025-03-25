def find_primes_in_range(a: int, b: int) -> list[int]:
    """
    Find all prime numbers within the given range (inclusive).

    Args:
        a (int): The lower bound of the range (inclusive)
        b (int): The upper bound of the range (inclusive)

    Returns:
        list[int]: A sorted list of prime numbers within the range

    Raises:
        ValueError: If a or b are negative or if a > b
    """
    # Validate input
    if a < 0 or b < 0:
        raise ValueError("Input range must contain non-negative integers")
    
    if a > b:
        raise ValueError("Lower bound must be less than or equal to upper bound")

    # Special case handling
    if a <= 1:
        a = 2

    # Sieve of Eratosthenes algorithm for finding primes
    def is_prime(n: int) -> bool:
        """Check if a number is prime using trial division."""
        if n < 2:
            return False
        
        # Only need to check up to square root of n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Find prime numbers in the range
    return sorted([num for num in range(a, b + 1) if is_prime(num)])