def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        str: The longest common substring. If no common substring exists, 
             returns an empty string. Matching is case-sensitive.

    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")

    # Handle empty string cases
    if not str1 or not str2:
        return ""

    # Find all common substrings with at least 2 characters
    common_substrings = []
    for i in range(len(str1)):
        for j in range(len(str2)):
            # Check substring starting at these positions
            k = 0
            while (i + k < len(str1) and 
                   j + k < len(str2) and 
                   str1[i + k] == str2[j + k]):
                k += 1
            
            # Add substring ONLY if it's at least 2 characters long
            substring = str1[i:i+k]
            if len(substring) > 1 and substring in str1 and substring in str2:
                common_substrings.append(substring)

    # Return the longest common substring, or empty string if none found
    return max(common_substrings, key=len, default="")