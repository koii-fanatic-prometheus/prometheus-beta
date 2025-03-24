import random
from typing import List, TypeVar

T = TypeVar('T')

def shuffle_array(arr: List[T]) -> List[T]:
    """
    Shuffle the elements of an input array randomly.
    
    This function uses the Fisher-Yates (Knuth) shuffle algorithm to 
    randomly reorder the elements of the input list in-place.
    
    Args:
        arr (List[T]): The input array to be shuffled.
    
    Returns:
        List[T]: A new list with the elements of the input array shuffled randomly.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    shuffled = arr.copy()
    
    # Fisher-Yates shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        
        # Swap elements
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled