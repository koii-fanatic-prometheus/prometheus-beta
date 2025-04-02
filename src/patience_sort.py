from typing import List, TypeVar, Any
import heapq

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
            # If the pile is empty or the top of the pile is greater than or equal to the item
            if not pile or (isinstance(pile[-1], type(item)) and item <= pile[-1]):
                pile.append(item)
                placed = True
                break
        
        # If no suitable pile is found, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge piles using a min-heap approach
    heap = [(pile[0], i, pile) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    result = []
    while heap:
        val, pile_index, pile = heapq.heappop(heap)
        result.append(val)
        pile.pop(0)
        
        # If the pile is not empty, push its new top element to the heap
        if pile:
            heapq.heappush(heap, (pile[0], pile_index, pile))
    
    return result