def to_alternating_constant_case(text):
    """
    Convert a string to alternating constant case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase and lowercase characters.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_constant_case("hello")
        'HeLlO'
        >>> to_alternating_constant_case("python")
        'PyThOn'
        >>> to_alternating_constant_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return as is
    if not text:
        return text
    
    # Convert to alternating case
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(text)
    )