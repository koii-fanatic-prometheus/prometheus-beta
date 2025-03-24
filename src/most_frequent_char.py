def find_most_frequent_char(input_string: str) -> str:
    """
    Find the most frequently occurring character in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character.
             If multiple characters have the same highest frequency, 
             returns the first such character in the string.
             Returns an empty string if the input is empty.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Count character frequencies
    char_freq = {}
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Find the most frequent character
    max_freq = 0
    most_frequent = input_string[0]  # Default to first character
    
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent = char
        # If frequencies are equal, keep the first occurrence
    
    return most_frequent