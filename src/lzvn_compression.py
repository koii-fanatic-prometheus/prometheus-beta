"""
Simple LZ-like Compression Algorithm Implementation

This module provides a basic implementation of a simple compression algorithm
that uses repeated sequence matching for compression.
"""

def lzvn_compress(data):
    """
    Compress input data using a simple LZ-like compression algorithm.
    
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
    
    compressed = bytearray()
    window_size = 4096
    current_pos = 0
    
    while current_pos < len(data):
        # Look for repeated sequence
        best_length = 0
        best_offset = 0
        
        # Search back in the window
        search_start = max(0, current_pos - window_size)
        for offset in range(current_pos - search_start):
            match_length = 0
            
            # Check match length
            while (current_pos + match_length < len(data) and 
                   data[current_pos - offset + match_length] == data[current_pos + match_length] and
                   match_length < 15):  # Limit match length to 4 bits
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = offset + 1
        
        # Encode data
        if best_length > 2:
            # Mark as match
            compressed.append(0xFF)  # Match marker
            compressed.append(best_offset & 0xFF)  # Offset low byte
            compressed.append(((best_offset >> 8) & 0x0F) | (best_length << 4))  # Offset high + length
            
            # Move past match
            current_pos += best_length
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return compressed

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed by the simple LZ-like algorithm.
    
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
    
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Check for match marker
        if (compressed_data[current_pos] == 0xFF and 
            current_pos + 2 < len(compressed_data)):
            # Match detected
            offset_low = compressed_data[current_pos + 1]
            control_byte = compressed_data[current_pos + 2]
            
            # Extract offset and length
            offset_high = control_byte & 0x0F
            length = (control_byte >> 4) & 0x0F
            
            # Reconstruct full offset
            offset = offset_low | (offset_high << 8)
            
            # Validate offset
            if offset <= len(decompressed):
                # Copy matched sequence
                match_start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[match_start + i])
            
            current_pos += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
    
    return decompressed