import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzc_compression import lzc_compress, lzc_decompress

def test_lzc_compress_basic():
    """Test basic compression of a simple string"""
    input_data = b"TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(input_data)
    assert isinstance(compressed, list)
    assert all(isinstance(code, int) for code in compressed)

def test_lzc_decompress_basic():
    """Test basic decompression of a compressed string"""
    input_data = b"TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(input_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed == input_data

def test_compress_decompress_roundtrip():
    """Verify that compress-decompress cycle preserves original data for various inputs"""
    test_cases = [
        b"hello world",
        b"aaaaabbbbbccccc",
        b"abcdefghijklmnopqrstuvwxyz",
        b"12345678901234567890"
    ]
    
    for test_input in test_cases:
        compressed = lzc_compress(test_input)
        decompressed = lzc_decompress(compressed)
        assert decompressed == test_input, f"Failed for input: {test_input}"

def test_string_input():
    """Test that the function works with string input"""
    input_data = "hello world"
    compressed = lzc_compress(input_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed == input_data.encode('utf-8')

def test_empty_input_compression():
    """Test handling of empty input during compression"""
    with pytest.raises(ValueError):
        lzc_compress(b"")
    with pytest.raises(ValueError):
        lzc_compress("")

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzc_compress(123)
    with pytest.raises(TypeError):
        lzc_compress(None)

def test_invalid_decompression_input():
    """Test handling of invalid decompression inputs"""
    with pytest.raises(TypeError):
        lzc_decompress("not a list")
    with pytest.raises(ValueError):
        lzc_decompress([])
    with pytest.raises(TypeError):
        lzc_decompress([1, 2, "invalid"])

def test_large_input():
    """Test compression of a larger input"""
    input_data = b"abcdefghijklmnopqrstuvwxyz" * 100
    compressed = lzc_compress(input_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed == input_data