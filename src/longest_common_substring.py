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

    # Find the best common substring
    best_substring = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            # Check substring starting at these positions
            k = 0
            current_substring = ""
            while (i + k < len(str1) and 
                   j + k < len(str2) and 
                   str1[i + k] == str2[j + k]):
                current_substring += str1[i + k]
                k += 1
            
            # Update best substring if current is longer and meets requirements
            if (len(current_substring) > len(best_substring) and 
                len(current_substring) > 1 and 
                str1.count(current_substring) > 0 and 
                str2.count(current_substring) > 0):
                best_substring = current_substring

    return best_substring