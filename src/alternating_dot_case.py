def to_alternating_dot_case(string):
    """
    Convert a string to alternating dot case.
    
    Args:
        string (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating dot case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_dot_case("hello world")
        'h.e.l.l.o. .w.o.r.l.d'
        >>> to_alternating_dot_case("python")
        'p.y.t.h.o.n'
        >>> to_alternating_dot_case("")
        ''
    """
    # Check input type
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not string:
        return ""
    
    # Convert to alternating dot case
    return '.'.join(
        char.lower() if i % 2 else char 
        for i, char in enumerate(string)
    )