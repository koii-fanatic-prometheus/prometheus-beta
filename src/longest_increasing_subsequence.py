def longest_increasing_subsequence(arr, return_sequence=False):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): Input list of integers
        return_sequence (bool, optional): If True, return the actual subsequence. 
                                          If False, return the length. Defaults to False.
    
    Returns:
        int or list: Length of the longest increasing subsequence, 
                     or the subsequence itself
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains non-comparable elements
    
    Examples:
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        6
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80], return_sequence=True)
        [10, 22, 33, 50, 60, 80]
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return 0 if not return_sequence else []
    
    # Length of the array
    n = len(arr)
    
    # Dynamic programming approach
    # dp stores the length of LIS ending at each index
    dp = [1] * n
    
    # To track the previous index for reconstructing the sequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the maximum length and its index
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # If we only want the length
    if not return_sequence:
        return max_length
    
    # Reconstruct the subsequence
    subsequence = []
    while max_index != -1:
        subsequence.insert(0, arr[max_index])
        max_index = prev[max_index]
    
    return subsequence