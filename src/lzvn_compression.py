"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of the LZVN (Lempel-Ziv Variable-length Number) compression algorithm.
LZVN is a variant of LZ compression used in some compression scenarios.

Key characteristics:
- Variable-length encoding
- Reduces redundancy in data by replacing repeated sequences with references
"""

def lzvn_compress(data):
    """
    Compress input data using LZVN compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to be compressed
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Initialize compression variables
    compressed = bytearray()
    window_size = 4096  # Standard window size for LZ-style compression
    current_pos = 0
    
    while current_pos < len(data):
        # Look for the longest match in the previous window
        best_length = 0
        best_offset = 0
        
        # Search back through the window for the longest match
        search_start = max(0, current_pos - window_size)
        for offset in range(current_pos - search_start):
            match_length = 0
            
            # Check how long the match continues
            while (current_pos + match_length < len(data) and 
                   data[current_pos - offset + match_length - 1] == data[current_pos + match_length]):
                match_length += 1
                
                # Prevent overrunning the data
                if match_length >= 255 or current_pos + match_length >= len(data):
                    break
            
            # Update best match if this is longer
            if match_length > best_length:
                best_length = match_length
                best_offset = offset + 1
        
        # Encode the match or literal
        if best_length > 2:
            # Encode match (offset, length)
            compressed.append(best_offset & 0xFF)  # Low byte of offset
            compressed.append((best_offset >> 8) & 0x0F)  # High 4 bits of offset
            compressed.append(best_length)  # Length of match
            current_pos += best_length
        else:
            # Encode literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return compressed

def lzvn_decompress(compressed_data):
    """
    Decompress data that was compressed using LZVN algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if len(compressed_data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Initialize decompression variables
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Check for literals first
        if current_pos + 2 >= len(compressed_data):
            # Remaining bytes are literals
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
            continue
        
        # Potential match: low byte of offset, high 4 bits of offset, length
        offset_low = compressed_data[current_pos]
        offset_high = compressed_data[current_pos + 1] & 0x0F
        offset = offset_low | (offset_high << 8)
        length = compressed_data[current_pos + 2]
        
        # If offset and length suggest a match, decode it
        if offset > 0 and length > 0:
            # Validate match parameters
            if offset > len(decompressed):
                decompressed.append(compressed_data[current_pos])
                current_pos += 1
                continue
            
            # Copy match from previous data
            match_start = len(decompressed) - offset
            for i in range(length):
                match_byte = decompressed[match_start + i]
                decompressed.append(match_byte)
            
            current_pos += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
    
    return decompressed