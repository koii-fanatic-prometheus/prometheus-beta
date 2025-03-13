import pytest
from src.sum_series import sum_series

def test_sum_series_positive_numbers():
    """Test sum_series with various positive inputs."""
    assert sum_series(5) == 15  # 1 + 2 + 3 + 4 + 5
    assert sum_series(10) == 55  # 1 + 2 + ... + 10
    assert sum_series(100) == 5050  # Sum of first 100 integers

def test_sum_series_zero():
    """Test sum_series with zero input."""
    assert sum_series(0) == 0

def test_sum_series_negative_input():
    """Test that sum_series raises ValueError for negative inputs."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_series(-1)

def test_sum_series_large_number():
    """Test sum_series with a large number to ensure performance."""
    # This should compute quickly due to constant time complexity
    large_n = 1_000_000
    expected = large_n * (large_n + 1) // 2
    assert sum_series(large_n) == expected