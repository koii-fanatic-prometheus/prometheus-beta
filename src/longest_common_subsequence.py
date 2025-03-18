def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Notes:
        - The function is case-sensitive
        - If multiple LCSs exist of same length, one is arbitrarily chosen
    """
    # Handle edge cases of empty strings
    if not str1 or not str2:
        return ''
    
    # Create a matrix to store lengths of common subsequences
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Strict case-sensitive comparison
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0  # No match allowed in case-sensitive scenario
    
    # Find the maximum subsequence length
    max_length = max(max(row) for row in dp)
    
    # If no common subsequence exists
    if max_length == 0:
        return ''
    
    # Find the position of the max length
    max_pos = None
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dp[i][j] == max_length:
                max_pos = (i, j)
                break
        if max_pos:
            break
    
    # Reconstruct the longest common subsequence
    if max_pos:
        i, j = max_pos
        lcs = []
        while i > 0 and j > 0 and dp[i][j] > 0:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        
        # Return the reversed subsequence (as we built it backwards)
        return ''.join(reversed(lcs))
    
    # Fallback (shouldn't happen)
    return ''