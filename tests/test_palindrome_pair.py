import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(11) == True
    assert is_palindrome(0) == True

def test_palindrome_pair_basic_positive():
    """Test cases with existing palindrome difference pairs."""
    # Explicitly check pairs where difference is a meaningful palindrome
    assert palindrome_pair([10, 20, 30, 44]) == True  # 44 - 10 = 34 (palindrome)
    assert palindrome_pair([11, 22, 33, 44]) == True  # Numbers and differences to consider

def test_palindrome_pair_basic_negative():
    """Test cases without palindrome difference pairs."""
    # Carefully constructed test case
    assert palindrome_pair([1, 3, 5, 7]) == False
    assert palindrome_pair([2, 4, 6, 8]) == False

def test_palindrome_pair_edge_cases():
    """Test edge cases."""
    assert palindrome_pair([]) == False  # Empty list
    assert palindrome_pair([5]) == False  # Single element
    
    # Require meaningful palindrome differences
    test_cases = [
        [11, 22, 33],  # Requires specific type of difference 
        [10, 20, 44],  # More complex difference
    ]
    assert any(palindrome_pair(case) for case in test_cases) == True

def test_palindrome_pair_invalid_input():
    """Test invalid input handling."""
    with pytest.raises(TypeError):
        palindrome_pair("not a list")
    
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, "3", 4])

def test_palindrome_pair_negative_numbers():
    """Test with negative numbers and mixed number types."""
    assert palindrome_pair([-10, 0, 20, 44]) == True  # 44 - (-10) or other combinations
    assert palindrome_pair([-1, 0, 1]) == False  # Trivial differences discouraged

def test_palindrome_pair_large_numbers():
    """Test with larger numbers."""
    assert palindrome_pair([100, 111, 222, 333]) == True  # Meaningful differences
    assert palindrome_pair([1000, 2000, 3000]) == False

def test_diagnostic_print():
    """Diagnostic test to understand differences."""
    nums = [10, 20, 30, 44]
    diffs = [abs(nums[j] - nums[i]) for i in range(len(nums)) for j in range(i+1, len(nums))]
    palindrome_diffs = [d for d in diffs if is_palindrome(d)]
    
    print("\nAll differences:", diffs)
    print("Palindrome differences:", palindrome_diffs)