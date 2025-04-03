def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a string containing lowercase and uppercase letters and spaces.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed input string
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input contains non-letter and non-space characters
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Check for invalid characters
    if not all(char.isalpha() or char.isspace() for char in s):
        raise ValueError("Input must contain only letters and spaces")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first character moved to end, rest of string recursively reversed
    return recursive_reverse_string(s[1:]) + s[0]