def lzc_compress(input_data):
    """
    Implement Lempel-Ziv-Cleary (LZC) compression algorithm.
    
    Args:
        input_data (str or bytes): The data to be compressed.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string or bytes object.
        ValueError: If input is empty.
    """
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes object")
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    result = []
    current_sequence = b''
    
    for byte in input_data:
        # Try to extend the current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If the sequence exists, keep extending
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            result.append(dictionary[current_sequence])
            
            # Add the new sequence to the dictionary
            if next_code < 65536:  # Limit dictionary size to 16-bit codes
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to the current byte
            current_sequence = bytes([byte])
    
    # Add the last sequence's code
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzc_decompress(compressed_data):
    """
    Decompress data that was compressed using the LZC algorithm.
    
    Args:
        compressed_data (list): List of integer codes to decompress.
    
    Returns:
        bytes: The decompressed data.
    
    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If input is empty or contains invalid codes.
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    result = []
    previous_code = compressed_data[0]
    result.extend(dictionary[previous_code])
    
    for code in compressed_data[1:]:
        if code not in dictionary:
            # Special case: code not yet in dictionary
            entry = dictionary[previous_code] + dictionary[previous_code][:1]
        else:
            entry = dictionary[code]
        
        # Add the entry to the result
        result.extend(entry)
        
        # Add a new dictionary entry if possible
        if next_code < 65536:  # Limit dictionary size to 16-bit codes
            dictionary[next_code] = dictionary[previous_code] + entry[:1]
            next_code += 1
        
        previous_code = code
    
    return bytes(result)