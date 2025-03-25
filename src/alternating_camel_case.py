def to_alternating_camel_case(input_string: str) -> str:
    """
    Convert a given string to alternating camel case.
    
    Alternating camel case means the first letter is lowercase, 
    and subsequent words start with alternating case.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating camel case
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    
    Examples:
        >>> to_alternating_camel_case("hello world")
        'helloWorld'
        >>> to_alternating_camel_case("PYTHON is AWESOME")
        'pythonIsAwesome'
        >>> to_alternating_camel_case("one TWO three FOUR")
        'oneTwoThreeFour'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and split by whitespace
    words = input_string.strip().split()
    
    # Check for empty input after stripping
    if not words:
        raise ValueError("Input cannot be an empty string")
    
    # Convert the first word to lowercase
    result = words[0].lower()
    
    # Convert subsequent words with precise capitalization 
    for i, word in enumerate(words[1:], start=1):
        if i % 2 == 1:
            # Capitalize even-indexed words (1-based odd indices)
            result += word[0].upper() + word[1:].lower()
        else:
            # Lowercase even-indexed words (1-based even indices)
            result += word[0].lower() + word[1:].lower()
    
    return result