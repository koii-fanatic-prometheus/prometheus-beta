import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from huffman_coding import (
    huffman_encode, 
    huffman_decode, 
    build_frequency_dict, 
    build_huffman_tree, 
    build_huffman_codes,
    HuffmanNode
)

def test_build_frequency_dict():
    """Test frequency dictionary creation."""
    text = "hello world"
    freq_dict = build_frequency_dict(text)
    assert freq_dict == {
        'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1
    }
    
    # Edge case: empty string
    assert build_frequency_dict("") == {}

def test_build_huffman_tree():
    """Test Huffman tree construction."""
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16}
    tree = build_huffman_tree(freq_dict)
    
    # Verify tree properties
    assert tree.freq == sum(freq_dict.values())
    
    # Test error handling
    with pytest.raises(ValueError):
        build_huffman_tree({})

def test_build_huffman_codes():
    """Test Huffman code generation."""
    # Create a simple tree
    root = HuffmanNode(None, 15)
    root.left = HuffmanNode('a', 5)
    root.right = HuffmanNode('b', 10)
    
    codes = build_huffman_codes(root)
    assert codes == {'a': '0', 'b': '1'}
    
    # Test with empty tree
    assert build_huffman_codes(None) == {}

def test_huffman_encode_decode():
    """Test full encode and decode process."""
    # Test various input scenarios
    test_cases = [
        "hello world",
        "abracadabra",
        "AAABBBCCCDDDEEE",
        "123456789",
        "A"
    ]
    
    for text in test_cases:
        # Encode
        encoded_data, huffman_tree = huffman_encode(text)
        
        # Decode
        decoded_text = huffman_decode(encoded_data, huffman_tree)
        
        # Verify
        assert decoded_text == text, f"Failed for input: {text}"

def test_error_handling():
    """Test error scenarios."""
    # Empty input
    with pytest.raises(ValueError):
        huffman_encode("")
    
    with pytest.raises(ValueError):
        huffman_decode("", None)
    
    # Invalid decode scenario
    with pytest.raises(ValueError):
        huffman_decode("1", HuffmanNode('a', 1))

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Single character
    text = "A"
    encoded_data, huffman_tree = huffman_encode(text)
    decoded_text = huffman_decode(encoded_data, huffman_tree)
    assert decoded_text == text
    
    # Repeated characters
    text = "AAAAAAA"
    encoded_data, huffman_tree = huffman_encode(text)
    decoded_text = huffman_decode(encoded_data, huffman_tree)
    assert decoded_text == text

def test_compression_efficiency():
    """Verify that Huffman coding reduces string length for repetitive data."""
    # Highly repetitive text
    text = "AAABBBCCCDDDEEE"
    
    # Encode
    encoded_data, _ = huffman_encode(text)
    
    # Verify shorter encoded length
    assert len(encoded_data) < len(text) * 8  # 8 bits per character in standard encoding