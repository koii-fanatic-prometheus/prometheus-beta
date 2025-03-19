import pytest
from src.modified_fibonacci import generate_modified_fibonacci

def test_modified_fibonacci_basic():
    """Test basic functionality of the modified Fibonacci sequence."""
    result = generate_modified_fibonacci(10)
    assert result == [1, 1, 3, 5], "Sequence should follow the modified Fibonacci constraints"

def test_modified_fibonacci_divisibility():
    """Verify that the sum of consecutive numbers is divisible by 3."""
    result = generate_modified_fibonacci(100)
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, \
            f"Sum of {result[i-2]} and {result[i-1]} should be divisible by 3"

def test_modified_fibonacci_edge_cases():
    """Test edge cases of the modified Fibonacci sequence generator."""
    assert generate_modified_fibonacci(0) == [], "Zero should return an empty list"
    assert generate_modified_fibonacci(1) == [1], "Input 1 should return [1]"
    assert generate_modified_fibonacci(2) == [1, 1], "Input 2 should return [1, 1]"

def test_modified_fibonacci_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_modified_fibonacci(-1)
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_modified_fibonacci("invalid")

def test_modified_fibonacci_large_input():
    """Test the function with a larger input."""
    result = generate_modified_fibonacci(1000)
    assert len(result) > 0, "Should generate a non-empty sequence"
    assert result[-1] <= 1000, "Last element should not exceed input"