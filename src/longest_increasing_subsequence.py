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
    
    # Specific sequence tracking
    specific_sequences = {
        0: [[arr[0]]]  # Start with first element in first slot
    }
    max_length = 1
    
    for i in range(1, n):
        # Potential best match from previous lengths
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
                
                # Add new sequences or update existing
                if lengths[i] not in specific_sequences:
                    specific_sequences[lengths[i]] = []
                
                # Generate potential sequences
                for seq in specific_sequences.get(lengths[i]-1, []):
                    new_seq = seq + [arr[i]]
                    if new_seq not in specific_sequences[lengths[i]]:
                        specific_sequences[lengths[i]].append(new_seq)
        
        # Update max length
        max_length = max(max_length, lengths[i])
    
    # Find the lexicographically smallest subsequence at max length
    candidates = specific_sequences.get(max_length, [])
    
    # If no candidates found, fallback to first element
    if not candidates:
        return 1, [arr[0]]
    
    # Select the lexicographically smallest sequence
    result = min(candidates, key=lambda x: (len(x), x))
    
    return len(result), result