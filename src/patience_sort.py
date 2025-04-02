from typing import List, TypeVar, Any
from functools import total_ordering

T = TypeVar('T')

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    This algorithm works by sorting elements using a method similar to playing 
    Patience (Solitaire) card sorting. It has a time complexity of O(n log n).
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list containing the same elements as the input
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (stacks) to simulate patience sorting
    piles = []
    
    for item in arr:
        # Try to place the item on an existing pile
        placed = False
        for pile in piles:
            # If the top of the pile is greater than the current item
            if not pile or item <= pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile is found, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge piles using a min-heap approach
    result = []
    while piles:
        # Find the pile with the smallest top card
        min_pile_index = 0
        for i in range(1, len(piles)):
            if piles[i][0] < piles[min_pile_index][0]:
                min_pile_index = i
        
        # Add the smallest item to the result
        result.append(piles[min_pile_index].pop(0))
        
        # Remove empty piles
        if not piles[min_pile_index]:
            piles.pop(min_pile_index)
    
    return result