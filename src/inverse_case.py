def convert_to_inverse_case(input_string):
    """
    Convert a string to inverse case.
    
    In inverse case, lowercase letters become uppercase,
    and uppercase letters become lowercase.
    Non-alphabetic characters remain unchanged.
    
    Args:
        input_string (str): The string to convert to inverse case
    
    Returns:
        str: The input string converted to inverse case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_inverse_case("Hello World!")
        'hELLO wORLD!'
        >>> convert_to_inverse_case("Python 3.9")
        'pYTHON 3.9'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to inverse case
    return input_string.swapcase()