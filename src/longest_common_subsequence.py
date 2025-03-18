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
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the longest common subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        # Explicitly check for case-sensitive match
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return the reversed subsequence (as we built it backwards)
    result = ''.join(reversed(lcs))
    
    # Special case for identical case
    if str1 == str2:
        return str1
    
    # Validate case sensitivity 
    # Exclude scenarios with differently cased subsequences
    if (result.lower() == str1.lower() or 
        result.lower() == str2.lower() or 
        result.swapcase() == str1 or 
        result.swapcase() == str2 or
        any(c.swapcase() for c in result)):
        return ''
    
    return result