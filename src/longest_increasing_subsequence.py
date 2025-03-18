from typing import List, Tuple

def find_longest_increasing_subsequence(arr: List[int]) -> Tuple[int, List[int]]:
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        Tuple[int, List[int]]: A tuple containing:
        - Length of the longest increasing subsequence
        - The longest increasing subsequence itself
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        (4, [2, 5, 7, 101])
        >>> find_longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
        (4, [0, 1, 2, 3])
        >>> find_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])
        (1, [7])
        >>> find_longest_increasing_subsequence([])
        (0, [])
    """
    # Handle empty input
    if not arr:
        return 0, []
    
    # Initialize dynamic programming arrays
    n = len(arr)
    # Length of LIS ending at each index
    lengths = [1] * n
    # Previous index for reconstruction
    prev_indices = [-1] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            # If current element can extend the subsequence
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
        
        # Update max length and index
        if lengths[i] > max_length or (lengths[i] == max_length and arr[i] < arr[max_index]):
            max_length = lengths[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current != -1:
        subsequence.append(arr[current])
        current = prev_indices[current]
    
    # Reverse to get correct order
    subsequence.reverse()
    
    return max_length, subsequence