"""
Simplified LZP-inspired Compression Algorithm Implementation

This module provides functions for a simplified compression and decompression
that uses basic context prediction techniques.
"""

class LZPCompressor:
    def __init__(self, context_length=8, dictionary_size=4096):
        """
        Initialize the LZP Compressor.
        
        :param context_length: Length of the context used for prediction
        :param dictionary_size: Size of the dictionary for context matching
        """
        self.context_length = context_length
        self.dictionary_size = dictionary_size

    def compress(self, data):
        """
        Compress the input data using a simplified LZP-like approach.
        
        :param data: Input data to compress (bytes or bytearray)
        :return: Compressed data
        """
        if not data:
            return bytearray()

        # Convert input to bytearray
        data = bytearray(data)
        compressed = bytearray()
        
        # If data is shorter than context, encode as is
        if len(data) <= self.context_length:
            for byte in data:
                compressed.extend([0, byte])  # Literal flag and byte
            return compressed
        
        # Encode first context_length bytes as literals
        for byte in data[:self.context_length]:
            compressed.extend([0, byte])
        
        # Initialize dictionary
        dictionary = {}
        
        # Process remaining data
        for i in range(self.context_length, len(data)):
            # Get current context
            context = bytes(data[i-self.context_length:i])
            
            # Check if context exists in dictionary
            if context in dictionary:
                # Compare next character to see if it's a matching pattern
                matches = dictionary[context]
                match_found = False
                
                for match_pos in matches:
                    if match_pos + 1 < len(data) and data[match_pos + 1] == data[i]:
                        # Encode as a match
                        compressed.append(1)  # Match flag
                        # Encode relative position (2 bytes)
                        rel_pos = abs(match_pos - (i - self.context_length))
                        compressed.extend(rel_pos.to_bytes(2, 'big'))
                        match_found = True
                        break
                
                # If no match found, encode as literal
                if not match_found:
                    compressed.extend([0, data[i]])
            else:
                # No context found, encode as literal
                compressed.extend([0, data[i]])
            
            # Update dictionary
            if context not in dictionary:
                dictionary[context] = []
            dictionary[context].append(i - 1)
            
            # Limit dictionary size
            if len(dictionary[context]) > self.dictionary_size:
                dictionary[context].pop(0)
        
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
        dictionary = {}
        
        i = 0
        while i < len(compressed_data):
            # Prevent index out of bounds
            if i + 1 >= len(compressed_data):
                break
            
            # Check compression type
            if compressed_data[i] == 1:  # Match
                # Ensure enough bytes for match
                if i + 3 > len(compressed_data):
                    break
                
                # Extract relative position
                rel_pos = int.from_bytes(compressed_data[i+1:i+3], 'big')
                
                # Calculate match position
                match_pos = len(decompressed) - rel_pos
                
                # Validate match position
                if match_pos < 0 or match_pos >= len(decompressed):
                    break
                
                # Retrieve matched byte
                matched_byte = decompressed[match_pos]
                decompressed.append(matched_byte)
                
                i += 3  # Flag + 2 bytes for position
            else:  # Literal
                # Validate literal byte exists
                if i + 1 >= len(compressed_data):
                    break
                
                # Append literal byte
                literal_byte = compressed_data[i+1]
                decompressed.append(literal_byte)
                
                i += 2  # Flag + literal byte
            
            # Update context dictionary
            if len(decompressed) >= self.context_length:
                context = bytes(decompressed[-self.context_length:])
                if context not in dictionary:
                    dictionary[context] = []
                dictionary[context].append(len(decompressed) - 1)
                
                # Limit dictionary size
                if len(dictionary[context]) > self.dictionary_size:
                    dictionary[context].pop(0)
        
        return decompressed