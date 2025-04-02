"""
Simple LZ-like Compression-Decompression Algorithm

This module provides a basic implementation of a data serialization and 
retrieval mechanism with minimal compression for learning purposes.
"""

def lzvn_compress(data):
    """
    Serialize input data with rudimentary compression-like marking.
    
    Args:
        data (bytes or bytearray): Input data to be compressed
    
    Returns:
        bytearray: Encoded data
    
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
    
    # Add data length as first 4 bytes
    compressed.extend(len(data).to_bytes(4, byteorder='big'))
    
    # Simple XOR encoding to mix data
    key = 0xAA  # Arbitrary encoding key
    for byte in data:
        compressed.append(byte ^ key)
    
    return compressed

def lzvn_decompress(compressed_data):
    """
    Deserialize data encoded by the simple algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty or invalid
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if len(compressed_data) < 4:
        raise ValueError("Input data is too short")
    
    # Recover original length
    original_length = int.from_bytes(compressed_data[:4], byteorder='big')
    
    # Decode data
    key = 0xAA  # Same key used in compression
    decompressed = bytearray()
    
    for byte in compressed_data[4:]:
        decompressed.append(byte ^ key)
    
    # Verify recovered length
    if len(decompressed) != original_length:
        raise ValueError("Data corruption detected")
    
    return decompressed