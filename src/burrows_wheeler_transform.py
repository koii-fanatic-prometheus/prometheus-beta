def burrows_wheeler_transform(text):
    """
    Implement the Burrows-Wheeler Transform for data compression.
    
    Args:
        text (str): Input string to be transformed
    
    Returns:
        tuple: A tuple containing the transformed string and the original index
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    # Add terminator character (not in original string)
    text += '$'
    
    # Generate all rotations of the input string
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Sort rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Find the original index and construct the transformed string
    original_index = sorted_rotations.index(text)
    transformed = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return transformed, original_index

def inverse_burrows_wheeler_transform(transformed, original_index):
    """
    Reverse the Burrows-Wheeler Transform.
    
    Args:
        transformed (str): Transformed string
        original_index (int): Original index from forward transform
    
    Returns:
        str: Reconstructed original string
    
    Raises:
        TypeError: If inputs are of incorrect type
        ValueError: If inputs are invalid
    """
    # Validate inputs
    if not isinstance(transformed, str) or not isinstance(original_index, int):
        raise TypeError("Invalid input types")
    
    if not transformed or original_index < 0 or original_index >= len(transformed):
        raise ValueError("Invalid transformed string or index")
    
    # Reconstruct the sorted first column 
    first_column = sorted(transformed)
    
    # Construct the last-first mapping
    table = [0] * len(transformed)
    char_count = {}
    
    for i, char in enumerate(transformed):
        if char not in char_count:
            char_count[char] = 0
        table[i] = char_count[char]
        char_count[char] += 1
    
    # Reconstruct the original string
    current_index = original_index
    result = []
    
    for _ in range(len(transformed)):
        result.append(first_column[current_index])
        current_index = table[current_index]
    
    # Remove terminator and return reconstructed string
    return ''.join(result[:-1])