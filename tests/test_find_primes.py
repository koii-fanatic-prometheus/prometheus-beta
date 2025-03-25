import pytest
from src.find_primes import find_primes_in_range

def test_find_primes_in_range_normal_case():
    """Test finding primes in a standard range."""
    assert find_primes_in_range(10, 30) == [11, 13, 17, 19, 23, 29]

def test_find_primes_in_range_lower_bound():
    """Test that range starts from a prime number."""
    assert find_primes_in_range(2, 10) == [2, 3, 5, 7]

def test_find_primes_in_range_single_prime():
    """Test a range with a single prime number."""
    assert find_primes_in_range(17, 17) == [17]

def test_find_primes_in_range_no_primes():
    """Test a range with no prime numbers."""
    assert find_primes_in_range(24, 26) == []

def test_find_primes_in_range_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input range must contain non-negative integers"):
        find_primes_in_range(-10, 10)

def test_find_primes_in_range_invalid_range():
    """Test that an invalid range (a > b) raises a ValueError."""
    with pytest.raises(ValueError, match="Lower bound must be less than or equal to upper bound"):
        find_primes_in_range(30, 10)

def test_find_primes_in_range_zero_and_one():
    """Verify behavior with lower bound less than 2."""
    assert find_primes_in_range(0, 10) == [2, 3, 5, 7]
    assert find_primes_in_range(1, 10) == [2, 3, 5, 7]