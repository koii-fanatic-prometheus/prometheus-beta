from typing import List, Tuple

def find_two_sum_pairs(numbers: List[int], target_sum: int) -> List[Tuple[int, int]]:
    """
    Find all unique pairs of numbers in the given array that sum up to the target.

    Args:
        numbers (List[int]): A list of unique integers to search through.
        target_sum (int): The target sum to find pairs for.

    Returns:
        List[Tuple[int, int]]: A list of tuples containing pairs of numbers that sum to the target.
        Each pair is returned only once, with the smaller number first.

    Raises:
        ValueError: If the input list is None or empty.
        TypeError: If the input is not a list of integers.
    """
    # Input validation
    if numbers is None:
        raise ValueError("Input list cannot be None")
    
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")

    # Use a hash set for O(n) time complexity
    result = []
    seen = set()

    for num in numbers:
        complement = target_sum - num
        
        # If the complement exists and we haven't already found this pair
        if complement in seen and complement != num:
            # Add the pair in sorted order to avoid duplicates
            pair = tuple(sorted((num, complement)))
            if pair not in result:
                result.append(pair)
        
        seen.add(num)

    return result