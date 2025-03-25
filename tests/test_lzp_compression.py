"""
Test suite for LZP Compression Algorithm
"""
import pytest
from src.lzp_compression import LZPCompressor

def test_lzp_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZPCompressor()
    original_data = bytearray(b'hello world hello world')
    
    # Compress
    compressed = compressor.compress(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed == original_data

def test_lzp_compression_empty_input():
    """Test compression and decompression with empty input"""
    compressor = LZPCompressor()
    
    # Empty input compression
    compressed_empty = compressor.compress(bytearray())
    assert compressed_empty == bytearray()
    
    # Empty input decompression
    decompressed_empty = compressor.decompress(bytearray())
    assert decompressed_empty == bytearray()

def test_lzp_compression_repeated_pattern():
    """Test compression with highly repetitive data"""
    compressor = LZPCompressor()
    original_data = bytearray(b'ABCABCABCABCABCABC')
    
    # Compress
    compressed = compressor.compress(original_data)
    assert compressed is not None
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed == original_data

def test_lzp_compression_binary_data():
    """Test compression with binary data"""
    compressor = LZPCompressor()
    original_data = bytearray(b'\x00\x01\x02\x03\x00\x01\x02\x03')
    
    # Compress
    compressed = compressor.compress(original_data)
    assert compressed is not None
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed == original_data

def test_lzp_compression_different_contexts():
    """Test compression with different context lengths"""
    # Test with small context
    compressor_small = LZPCompressor(context_length=4)
    original_data = bytearray(b'hello world hello universe')
    
    compressed_small = compressor_small.compress(original_data)
    decompressed_small = compressor_small.decompress(compressed_small)
    assert decompressed_small == original_data
    
    # Test with large context
    compressor_large = LZPCompressor(context_length=16)
    compressed_large = compressor_large.compress(original_data)
    decompressed_large = compressor_large.decompress(compressed_large)
    assert decompressed_large == original_data

def test_lzp_compression_large_input():
    """Test compression with larger input"""
    compressor = LZPCompressor()
    original_data = bytearray(b'This is a longer test string with some repetitive content ' * 10)
    
    # Compress
    compressed = compressor.compress(original_data)
    assert compressed is not None
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed == original_data