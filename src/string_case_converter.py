def to_kebab_case(text: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Kebab case transforms the input string to lowercase with words separated by hyphens.
    Handles various input formats including camelCase, snake_case, and mixed strings.
    
    Args:
        text (str): The input string to convert to kebab-case.
    
    Returns:
        str: The input string converted to kebab-case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_kebab_case("HelloWorld")
        'hello-world'
        >>> to_kebab_case("hello_world")
        'hello-world'
        >>> to_kebab_case("Hello World")
        'hello-world'
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not text:
        return ""
    
    # Replace non-alphanumeric characters with hyphens
    import re
    
    # Convert camelCase and PascalCase to kebab-case
    # Replace capital letters with hyphen + lowercase
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', text)
    
    # Replace underscores, spaces, and multiple consecutive non-alphanumeric chars with single hyphen
    text = re.sub(r'[_\s]+', '-', text)
    
    # Remove any non-alphanumeric characters except hyphens
    text = re.sub(r'[^a-z0-9-]', '', text.lower())
    
    # Remove consecutive hyphens
    text = re.sub(r'-+', '-', text)
    
    # Remove leading and trailing hyphens
    text = text.strip('-')
    
    return text