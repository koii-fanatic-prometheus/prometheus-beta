def can_convert_by_one_deletion(word1: str, word2: str) -> bool:
    """
    Determines if word1 can be converted to word2 by deleting exactly one character.
    
    Args:
        word1 (str): The first word
        word2 (str): The target word
    
    Returns:
        bool: True if word1 can be converted to word2 by deleting exactly one character, False otherwise
    
    Raises:
        TypeError: If inputs are not strings
    
    Examples:
        >>> can_convert_by_one_deletion("abcd", "abc")  # delete 'd'
        True
        >>> can_convert_by_one_deletion("abcd", "abcde")
        False
        >>> can_convert_by_one_deletion("a", "")
        True
    """
    # Type checking
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Both inputs must be strings")
    
    # Handle trivial length differences
    if len(word1) != len(word2) + 1:
        return False
    
    # Try removing each character and check if the result matches word2
    for i in range(len(word1)):
        candidate = word1[:i] + word1[i+1:]
        if candidate == word2:
            return True
    
    return False