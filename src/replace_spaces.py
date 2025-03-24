def replace_spaces_with_underscores(input_string: str) -> str:
    """
    Replace all spaces in a given string with underscores.

    Args:
        input_string (str): The input string to modify.

    Returns:
        str: A new string with all spaces replaced by underscores.

    Examples:
        >>> replace_spaces_with_underscores("hello world")
        'hello_world'
        >>> replace_spaces_with_underscores("  multiple   spaces  ")
        '__multiple___spaces__'
        >>> replace_spaces_with_underscores("")
        ''
    """
    if input_string is None:
        raise ValueError("Input string cannot be None")
    
    return input_string.replace(" ", "_")