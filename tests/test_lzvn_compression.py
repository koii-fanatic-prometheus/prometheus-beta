"""
Test suite for LZVN Compression Algorithm

This test suite covers various scenarios for the LZVN compression and decompression functions.
"""

import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzvn_compression import lzvn_compress, lzvn_decompress

def test_compress_decompress_basic():
    """Test basic compression and decompression with a simple string."""
    original_data = bytearray(b'Hello, world! Hello, world!')
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_compress_decompress_repeated_pattern():
    """Test compression with a highly repetitive pattern."""
    original_data = bytearray(b'ABCABCABCABCABCABC' * 10)
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_compress_decompress_binary_data():
    """Test compression with binary data."""
    original_data = bytearray(range(256)) * 5
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzvn_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzvn_decompress("not bytes")

def test_empty_input():
    """Test error handling for empty input."""
    with pytest.raises(ValueError):
        lzvn_compress(bytearray())
    
    with pytest.raises(ValueError):
        lzvn_decompress(bytearray())

def test_no_compression_needed():
    """Test data that cannot be effectively compressed."""
    original_data = bytearray(os.urandom(1000))  # Random data
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_large_data():
    """Test compression and decompression of large data."""
    original_data = bytearray(b'TestData') * 10000
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_compression_ratio():
    """Verify that compression reduces data size for repetitive data."""
    original_data = bytearray(b'REPEAT' * 1000)
    compressed = lzvn_compress(original_data)
    
    assert len(compressed) < len(original_data)

def test_symmetry():
    """Ensure compression and decompression are symmetrical."""
    original_data = bytearray(b'Test compression symmetry' * 100)
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data
    assert lzvn_decompress(lzvn_compress(decompressed)) == decompressed