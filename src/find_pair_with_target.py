def find_pair_with_target(nums, target):
    """
    Find index pairs of numbers that sum up to the target in a list of unique integers.

    Args:
        nums (list): A list of unique integers.
        target (int): The target sum to find.

    Returns:
        list: A list of index pairs where the numbers at those indices sum to the target.
               Returns an empty list if no such pairs exist.

    Raises:
        TypeError: If inputs are not of the expected types.
        ValueError: If nums is empty.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list")
    if not isinstance(target, int):
        raise TypeError("Input 'target' must be an integer")
    
    # Check for empty list
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Use a hash map to store first indices of each number
    first_indices = {}
    result = []
    
    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in previous indices
        if complement in first_indices:
            # Generate all possible pairs with this complement and current number
            for j in first_indices[complement]:
                pair = tuple(sorted([j, i]))
                if pair not in result:
                    result.append(pair)
        
        # Add current index to the list of indices for this number
        if num not in first_indices:
            first_indices[num] = []
        first_indices[num].append(i)
    
    # Return unique pairs sorted
    return sorted(result)