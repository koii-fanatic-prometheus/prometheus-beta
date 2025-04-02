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
    
    # Ensure all elements are of the same type
    if not all(isinstance(x, type(arr[0])) for x in arr):
        raise TypeError("All elements must be of the same type")
    
    # Create piles (stacks) in Patience Sort
    piles = []
    
    for item in arr:
        # Find the correct pile to place the item
        found_pile = False
        for pile in piles:
            # Attempt to place on first pile where the top item is >= current item
            if not pile or item <= pile[-1]:
                pile.append(item)
                found_pile = True
                break
        
        # If no existing pile works, create a new pile
        if not found_pile:
            piles.append([item])
    
    # Merge piles using a min-heap
    result = []
    heap = [(pile[0], i) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    # Track the piles
    while heap:
        val, pile_index = heapq.heappop(heap)
        result.append(val)
        
        # Remove the top item from its pile
        piles[pile_index].pop(0)
        
        # If the pile is not empty, add its new top to the heap
        if piles[pile_index]:
            heapq.heappush(heap, (piles[pile_index][0], pile_index))
    
    return result