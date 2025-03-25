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
    
    # Create first and last column
    first_column = sorted(transformed)
    
    # Create mapping array
    n = len(transformed)
    next_index = [0] * n
    char_count = {}
    
    # Prepare count dictionary for each character
    char_freq = {}
    for char in transformed:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Compute next index using first and last columns
    for i in range(n):
        current_char = transformed[i]
        
        # Find the position of this occurrence of current_char in first column
        if current_char not in char_count:
            char_count[current_char] = 0
        
        # Find the next index by counting occurrences
        next_index[i] = first_column.index(current_char, char_count[current_char])
        char_count[current_char] += 1
    
    # Reconstruct the original string
    result = []
    current_index = original_index
    
    for _ in range(n - 1):  # Exclude terminator
        result.append(transformed[current_index])
        current_index = next_index[current_index]
    
    return ''.join(result[::-1])  # Reverse to get original string