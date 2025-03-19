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
    assert palindrome_pair([10, 22, 44, 66]) == True  # 44 - 10 = 34 (palindrome)
    assert palindrome_pair([110, 122, 144, 166]) == True  # Large numbers with palindrome diff

def test_palindrome_pair_basic_negative():
    """Test cases without palindrome difference pairs."""
    assert palindrome_pair([1, 3, 5, 7]) == False  # Small differences
    assert palindrome_pair([2, 4, 6, 8]) == False  # No palindrome differences

def test_palindrome_pair_edge_cases():
    """Test edge cases."""
    assert palindrome_pair([]) == False  # Empty list
    assert palindrome_pair([5]) == False  # Single element
    assert palindrome_pair([10, 20, 30, 44]) == True  # Larger meaningful difference

def test_palindrome_pair_invalid_input():
    """Test invalid input handling."""
    with pytest.raises(TypeError):
        palindrome_pair("not a list")
    
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, "3", 4])

def test_palindrome_pair_negative_numbers():
    """Test with negative numbers and mixed number types."""
    assert palindrome_pair([-10, 0, 22, 44]) == True  # Large palindrome difference
    assert palindrome_pair([-1, 0, 1]) == False  # Trivial differences

def test_palindrome_pair_large_numbers():
    """Test with larger numbers."""
    assert palindrome_pair([100, 111, 222, 333]) == True
    assert palindrome_pair([1000, 2000, 3000]) == False

def test_diagnostic_print():
    """Diagnostic test to understand differences."""
    nums = [10, 22, 44, 66]
    diffs = [abs(nums[j] - nums[i]) for i in range(len(nums)) for j in range(i+1, len(nums))]
    palindrome_diffs = [d for d in diffs if is_palindrome(d)]
    
    print("\nAll differences:", diffs)
    print("Palindrome differences:", palindrome_diffs)