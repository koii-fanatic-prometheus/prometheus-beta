def can_partition_equal_sum(numbers):
    """
    Determine if a list of integers can be split into two sublists 
    with equal total sum.

    Args:
        numbers (list): A list of integers to be partitioned.

    Returns:
        bool: True if the list can be split into two sublists with equal sum, 
              False otherwise.

    Examples:
        >>> can_partition_equal_sum([1, 5, 11, 5])
        True
        >>> can_partition_equal_sum([1, 2, 3, 5])
        False
    """
    # Handle edge cases
    if not numbers:
        return False
    
    total_sum = sum(numbers)
    
    # If total sum is odd, equal partition is impossible
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Initialize dynamic programming table
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    # Build subset sum solution
    for num in numbers:
        for j in range(target_sum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target_sum]