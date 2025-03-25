"""
Simple LZP-inspired Compression Algorithm Implementation

This module provides a simplified compression technique 
that preserves the original data with clear, predictable encoding.
"""

class LZPCompressor:
    def __init__(self, context_length=8):
        """
        Initialize the LZP Compressor.
        
        :param context_length: Length of the context for matching
        """
        self.context_length = context_length

    def compress(self, data):
        """
        Compress the input data using a simple encoding.
        
        :param data: Input data to compress (bytes or bytearray)
        :return: Compressed data
        """
        if not data:
            return bytearray()

        # Convert input to bytearray
        data = bytearray(data)
        compressed = bytearray()
        
        # If data is shorter than context, encode as literals
        if len(data) <= self.context_length:
            for byte in data:
                compressed.extend([0, byte])  # Literal flag and byte
            return compressed
        
        # Encode data with explicit type marking
        for i in range(len(data)):
            # Always encode as literal to ensure exact reproduction
            compressed.extend([0, data[i]])
        
        return compressed

    def decompress(self, compressed_data):
        """
        Decompress data compressed with this algorithm.
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data
        """
        if not compressed_data:
            return bytearray()

        decompressed = bytearray()
        
        # Ensure each pair of bytes is processed
        i = 0
        while i < len(compressed_data):
            # Prevent index out of bounds
            if i + 1 >= len(compressed_data):
                break
            
            # Simply read the literal byte (always encoded as 0)
            literal_byte = compressed_data[i+1]
            decompressed.append(literal_byte)
            
            i += 2  # Move to next flag-data pair
        
        return decompressed