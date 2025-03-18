def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
    """
    # Handle edge cases
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Remove whitespace and convert to lowercase for consistent comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Use character frequency counting with sorting that works with Unicode
    return sorted(list(str1)) == sorted(list(str2))