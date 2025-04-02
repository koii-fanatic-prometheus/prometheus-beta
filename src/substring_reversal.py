def reverse_substring(s: str, start: int, end: int) -> str:
    """
    Reverse a substring of a given string within specified start and end indices.

    Args:
        s (str): The input string to modify
        start (int): The starting index of the substring to reverse (inclusive)
        end (int): The ending index of the substring to reverse (exclusive)

    Returns:
        str: A new string with the specified substring reversed

    Raises:
        ValueError: If start or end indices are out of bounds
        TypeError: If inputs are not of the correct type
    """
    # Type checking
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers")
    
    # Special case for empty string
    if len(s) == 0:
        if start == 0 and end == 0:
            return s
        raise ValueError("Invalid substring indices")
    
    # Bounds checking
    if start < 0 or end > len(s) or start >= end:
        raise ValueError("Invalid substring indices")
    
    # Construct the reversed substring
    return s[:start] + s[start:end][::-1] + s[end:]