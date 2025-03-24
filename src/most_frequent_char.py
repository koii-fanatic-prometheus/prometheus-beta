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
    first_occurrence = {}
    
    for idx, char in enumerate(input_string):
        # Track first occurrence index
        if char not in first_occurrence:
            first_occurrence[char] = idx
        
        # Count frequencies
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Find the most frequent character
    max_freq = 0
    most_frequent = input_string[0]  # Default to first character
    
    for char, freq in char_freq.items():
        # If frequency is higher, update
        if freq > max_freq:
            max_freq = freq
            most_frequent = char
        # If frequencies are equal, compare first occurrence index
        elif freq == max_freq and first_occurrence[char] < first_occurrence[most_frequent]:
            most_frequent = char
    
    return most_frequent