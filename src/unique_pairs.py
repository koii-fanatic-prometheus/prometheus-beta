from typing import List, Tuple

def find_unique_pairs(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Find all unique pairs of elements from the given list of integers.
    
    A unique pair is defined as a combination of two different elements, 
    where the order doesn't matter (i.e., (a, b) is the same as (b, a)).
    
    Args:
        numbers (List[int]): Input list of integers
    
    Returns:
        List[Tuple[int, int]]: List of unique pairs of integers
    
    Examples:
        >>> find_unique_pairs([1, 2, 3, 4])
        [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        
        >>> find_unique_pairs([])
        []
        
        >>> find_unique_pairs([1])
        []
    """
    # Handle edge cases
    if len(numbers) < 2:
        return []
    
    # Use set to track unique pairs and avoid duplicates
    unique_pairs = set()
    
    # Use a set of unique numbers to avoid duplicate pairs
    unique_numbers = set(numbers)
    
    # Generate pairs using sorted list of unique numbers
    unique_list = sorted(unique_numbers)
    
    # Generate pairs using nested loop
    for i in range(len(unique_list)):
        for j in range(i + 1, len(unique_list)):
            unique_pairs.add((unique_list[i], unique_list[j]))
    
    return list(unique_pairs)