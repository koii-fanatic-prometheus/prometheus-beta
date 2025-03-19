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
    
    # Use a hash map to store complements
    complement_map = {}
    result = []
    
    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists and came before current number
        if complement in complement_map:
            # Store the pair based on original indices
            pair = tuple(sorted([complement_map[complement], i]))
            if pair not in result:
                result.append(pair)
        
        # Store current number's index (first occurrence)
        if num not in complement_map:
            complement_map[num] = i
    
    # Return unique pairs sorted
    return sorted(result)