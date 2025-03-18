def run_length_encode(data):
    """
    Implement Run-Length Encoding (RLE) for data compression.
    
    Args:
        data (str or list): Input sequence to be compressed
    
    Returns:
        list: Compressed sequence of [character, count] pairs
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input is an empty sequence
    """
    # Validate input
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # Convert string to list if necessary
    if isinstance(data, str):
        data = list(data)
    
    # Compression logic
    compressed = []
    if not data:
        return compressed
    
    current_char = data[0]
    current_count = 1
    
    for char in data[1:]:
        if char == current_char:
            current_count += 1
        else:
            compressed.append([current_char, current_count])
            current_char = char
            current_count = 1
    
    # Add the last run
    compressed.append([current_char, current_count])
    
    return compressed

def run_length_decode(compressed):
    """
    Decode a Run-Length Encoded sequence.
    
    Args:
        compressed (list): Compressed sequence of [character, count] pairs
    
    Returns:
        list: Decompressed sequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input is malformed
    """
    # Validate input
    if not isinstance(compressed, list):
        raise TypeError("Input must be a list of [character, count] pairs")
    
    # Decompression logic
    decompressed = []
    
    for item in compressed:
        # Validate each item
        if not (isinstance(item, list) and len(item) == 2 and 
                isinstance(item[0], (str, int)) and isinstance(item[1], int)):
            raise ValueError("Each item must be [character, count]")
        
        char, count = item
        decompressed.extend([char] * count)
    
    return decompressed