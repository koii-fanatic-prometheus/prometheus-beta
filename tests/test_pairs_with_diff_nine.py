import os
import pytest
from src.pairs_with_diff_nine import find_sum_of_pairs_with_diff_nine

def test_basic_pair_sum():
    """Test basic case with straightforward pairs"""
    # Create a temp file with numbers
    with open('test_numbers.txt', 'w') as f:
        f.write("1\n10\n5\n14\n20\n29\n")
    
    # 1 and 10 form a pair, 5 and 14 form a pair
    assert find_sum_of_pairs_with_diff_nine('test_numbers.txt') == (1+10) + (5+14)
    
    # Clean up
    os.remove('test_numbers.txt')

def test_duplicate_pairs():
    """Test case with duplicate pairs"""
    with open('test_numbers.txt', 'w') as f:
        f.write("1\n10\n1\n10\n5\n14\n")
    
    # Should only count unique pairs
    assert find_sum_of_pairs_with_diff_nine('test_numbers.txt') == (1+10) + (5+14)
    
    # Clean up
    os.remove('test_numbers.txt')

def test_empty_file():
    """Test empty file case"""
    with open('test_numbers.txt', 'w') as f:
        f.write("")
    
    assert find_sum_of_pairs_with_diff_nine('test_numbers.txt') == 0
    
    # Clean up
    os.remove('test_numbers.txt')

def test_file_not_found():
    """Test file not found error"""
    with pytest.raises(FileNotFoundError):
        find_sum_of_pairs_with_diff_nine('nonexistent_file.txt')

def test_invalid_content():
    """Test file with non-numeric content"""
    with open('test_numbers.txt', 'w') as f:
        f.write("1\n10\nabc\n14\n")
    
    with pytest.raises(ValueError):
        find_sum_of_pairs_with_diff_nine('test_numbers.txt')
    
    # Clean up
    os.remove('test_numbers.txt')

def test_single_number():
    """Test file with single number"""
    with open('test_numbers.txt', 'w') as f:
        f.write("10\n")
    
    assert find_sum_of_pairs_with_diff_nine('test_numbers.txt') == 0
    
    # Clean up
    os.remove('test_numbers.txt')

def test_multiple_pairs():
    """Test file with multiple valid pairs"""
    with open('test_numbers.txt', 'w') as f:
        f.write("1\n10\n5\n14\n20\n29\n38\n47\n")
    
    # Expected pairs: (1,10), (5,14), (20,29), (38,47)
    expected_sum = (1+10) + (5+14) + (20+29) + (38+47)
    assert find_sum_of_pairs_with_diff_nine('test_numbers.txt') == expected_sum
    
    # Clean up
    os.remove('test_numbers.txt')