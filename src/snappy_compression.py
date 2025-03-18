"""
Snappy Compression Algorithm Implementation

This module provides a simplified implementation of the Snappy compression algorithm.
Snappy is a fast compression/decompression library developed by Google.

Note: This is a basic implementation and does not fully replicate the original Snappy algorithm.
For production use, consider using the official snappy library.
"""

def snappy_compress(data):
    """
    Compress input data using a simplified Snappy-like compression algorithm.
    
    Args:
        data (bytes or str): Input data to compress
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # Simple compression strategy
    compressed = bytearray()
    
    # Literal encoding with basic run-length encoding
    i = 0
    while i < len(data):
        # Look for repeating bytes
        repeat_count = 1
        while (i + repeat_count < len(data) and 
               repeat_count < 255 and 
               data[i] == data[i + repeat_count]):
            repeat_count += 1
        
        # If repeated more than 2 times, use run-length encoding
        if repeat_count > 2:
            compressed.append(0xFF)  # Special marker for run-length
            compressed.append(repeat_count)
            compressed.append(data[i])
            i += repeat_count
        else:
            # Literal byte(s)
            if i + 2 < len(data) and data[i] == data[i+1] == data[i+2]:
                # Start of a potential repeat sequence
                compressed.append(0xFE)  # Pre-repeat marker
                compressed.append(data[i])
            compressed.append(data[i])
            i += 1
    
    # Ensure we always produce at least a slightly different output
    if len(compressed) == len(data):
        compressed.append(0x00)  # Add a marker to indicate minimal compression
    
    return bytes(compressed)

def snappy_decompress(compressed_data):
    """
    Decompress data compressed with the simplified Snappy-like algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or malformed
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decompression
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check for run-length encoding marker
        if compressed_data[i] == 0xFF:
            if i + 2 >= len(compressed_data):
                raise ValueError("Malformed compressed data")
            
            # Extract repeat count and byte
            repeat_count = compressed_data[i + 1]
            repeat_byte = compressed_data[i + 2]
            
            # Add repeated bytes
            decompressed.extend([repeat_byte] * repeat_count)
            
            # Move index
            i += 3
        elif compressed_data[i] == 0xFE:
            # Pre-repeat marker (3 identical bytes)
            if i + 1 >= len(compressed_data):
                raise ValueError("Malformed compressed data")
            
            # Add 3 repeated bytes
            repeat_byte = compressed_data[i + 1]
            decompressed.extend([repeat_byte] * 3)
            
            # Move index
            i += 2
        elif compressed_data[i] == 0x00 and len(compressed_data) > 1:
            # Minimal compression marker
            i += 1
            break
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return bytes(decompressed)