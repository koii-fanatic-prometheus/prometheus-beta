"""
Tests for Snappy Compression Algorithm Implementation
"""

import pytest
from src.snappy_compression import snappy_compress, snappy_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original = b"hello world"
    compressed = snappy_compress(original)
    assert compressed != original
    decompressed = snappy_decompress(compressed)
    assert decompressed == original

def test_repeated_bytes_compression():
    """Test compression of repeated bytes"""
    original = b"aaaaaabbbbbb"
    compressed = snappy_compress(original)
    assert len(compressed) < len(original)
    decompressed = snappy_decompress(compressed)
    assert decompressed == original

def test_string_input():
    """Test compression with string input"""
    original = "Hello, Snappy Compression!"
    compressed = snappy_compress(original)
    decompressed = snappy_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_empty_input_raises_error():
    """Test that empty input raises ValueError"""
    with pytest.raises(ValueError):
        snappy_compress(b"")
    with pytest.raises(ValueError):
        snappy_decompress(b"")

def test_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        snappy_compress(123)
    with pytest.raises(TypeError):
        snappy_decompress(123)

def test_complex_data():
    """Test compression with more complex data"""
    original = b"This is a test of the Snappy compression algorithm with some repeated bytes like aaaabbbbcccc"
    compressed = snappy_compress(original)
    assert len(compressed) < len(original)
    decompressed = snappy_decompress(compressed)
    assert decompressed == original

def test_binary_data():
    """Test compression with binary data"""
    original = bytes([0, 1, 2, 3, 4, 5, 0, 0, 0, 1, 1, 1])
    compressed = snappy_compress(original)
    decompressed = snappy_decompress(compressed)
    assert decompressed == original