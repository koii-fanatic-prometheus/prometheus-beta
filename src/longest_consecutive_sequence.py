def find_longest_consecutive_sequence(nums):
    """
    Find the longest consecutive sequence of numbers in the given list.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        list: The longest consecutive sequence of numbers
    
    Examples:
        >>> find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
        [1, 2, 3, 4]
        >>> find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    # Handle empty list edge case
    if not nums:
        return []
    
    # Convert to set for O(1) lookup
    num_set = set(nums)
    
    longest_sequence = []
    is_consecutive_found = False
    
    for num in num_set:
        # Check if this number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = [current_num]
            
            # Extend the sequence as long as consecutive numbers exist
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence.append(current_num)
                is_consecutive_found = True
            
            # Update longest sequence if current is longer
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
    
    # If no consecutive sequence found, return the smallest number
    return longest_sequence if is_consecutive_found else [min(nums)]