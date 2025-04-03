def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        str: The longest common substring. If no common substring exists, 
             returns an empty string.

    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")

    # Handle empty string cases
    if not str1 or not str2:
        return ""

    # Dynamic programming approach to find longest common substring
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the maximum length and ending position
    max_length = 0
    end_position = 0

    # Fill the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Case-sensitive exact match
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and ending position if needed
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i - 1
    
    # Extract and return the longest common substring
    if max_length == 0:
        # No common substring found
        return ""
    
    substring = str1[end_position - max_length + 1:end_position + 1]
    
    # Ensure the substring is long enough and actually appears in both strings
    if len(substring) > 1 and substring in str1 and substring in str2:
        return substring
    
    return ""