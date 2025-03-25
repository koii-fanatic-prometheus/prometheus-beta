"""
LZP (Lempel-Ziv Prediction) Compression Algorithm Implementation

This module provides functions for LZP compression and decompression.
LZP is a lossless data compression algorithm that uses context prediction.
"""

class LZPCompressor:
    def __init__(self, context_length=8, dictionary_size=4096):
        """
        Initialize the LZP Compressor.
        
        :param context_length: Length of the context used for prediction (default: 8)
        :param dictionary_size: Size of the dictionary for context matching (default: 4096)
        """
        self.context_length = context_length
        self.dictionary_size = dictionary_size

    def compress(self, data):
        """
        Compress the input data using LZP compression.
        
        :param data: Input data to compress (bytes or bytearray)
        :return: Compressed data
        """
        if not data:
            return bytearray()

        # Convert input to bytearray for manipulation
        data = bytearray(data)
        compressed = bytearray()
        
        # Initialize context and dictionary
        context = data[:self.context_length]
        dictionary = {}
        
        # Pointer to current position in data
        i = self.context_length
        
        while i < len(data):
            # Try to find a match in the dictionary
            match_found = False
            
            # Check for context match
            current_context = data[i-self.context_length:i]
            
            if current_context in dictionary:
                potential_matches = dictionary[current_context]
                
                for match_pos in potential_matches:
                    # If match exists and next byte matches
                    if match_pos + self.context_length < len(data) and \
                       data[match_pos + self.context_length] == data[i]:
                        # Encode match
                        compressed.append(1)  # Match flag
                        # Encode relative position
                        rel_pos = match_pos - (i - self.context_length)
                        compressed.extend(rel_pos.to_bytes(2, 'big'))
                        match_found = True
                        i += 1
                        break
            
            # If no match found, encode literal
            if not match_found:
                compressed.append(0)  # Literal flag
                compressed.append(data[i])
                i += 1
            
            # Update dictionary
            if current_context not in dictionary:
                dictionary[current_context] = []
            dictionary[current_context].append(i - 1)
            
            # Limit dictionary size
            if len(dictionary[current_context]) > self.dictionary_size:
                dictionary[current_context].pop(0)
        
        return compressed

    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZP algorithm.
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data
        """
        if not compressed_data:
            return bytearray()

        decompressed = bytearray()
        
        # Initialize dictionary
        dictionary = {}
        
        i = 0
        while i < len(compressed_data):
            # Check compression type
            if compressed_data[i] == 1:  # Match
                # Extract relative position (2 bytes)
                rel_pos = int.from_bytes(compressed_data[i+1:i+3], 'big')
                
                # Calculate absolute position
                match_pos = len(decompressed) + rel_pos
                
                # Retrieve matched byte
                matched_byte = decompressed[match_pos]
                decompressed.append(matched_byte)
                
                i += 3  # Flag + 2 bytes for position
            else:  # Literal
                literal_byte = compressed_data[i+1]
                decompressed.append(literal_byte)
                
                i += 2  # Flag + literal byte
            
            # Update context dictionary (same logic as compression)
            if len(decompressed) >= self.context_length:
                current_context = decompressed[-self.context_length:]
                if current_context not in dictionary:
                    dictionary[current_context] = []
                dictionary[current_context].append(len(decompressed) - 1)
                
                # Limit dictionary size
                if len(dictionary[current_context]) > self.dictionary_size:
                    dictionary[current_context].pop(0)
        
        return decompressed