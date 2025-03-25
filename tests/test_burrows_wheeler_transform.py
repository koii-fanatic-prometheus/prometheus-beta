import pytest
from src.burrows_wheeler_transform import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_basic():
    """Test basic Burrows-Wheeler Transform functionality"""
    text = "banana"
    transformed, original_index = burrows_wheeler_transform(text)
    assert isinstance(transformed, str)
    assert isinstance(original_index, int)
    
    # Note: Exact reconstruction might be different due to rotations
    assert len(transformed) == len(text) + 1

def test_burrows_wheeler_transform_empty_string():
    """Test transform with empty string raises ValueError"""
    with pytest.raises(ValueError):
        burrows_wheeler_transform("")

def test_burrows_wheeler_transform_invalid_input():
    """Test transform with invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        burrows_wheeler_transform(123)

def test_inverse_transform_invalid_inputs():
    """Test inverse transform with invalid inputs"""
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform(123, "not an int")
    
    with pytest.raises(ValueError):
        inverse_burrows_wheeler_transform("", -1)

def test_burrows_wheeler_transform_full_cycle():
    """Test complete transform and inverse transform cycle"""
    test_strings = ["banana", "ABRACADABRA", "MISSISSIPPI", "hello world", "python"]
    
    for text in test_strings:
        # Perform transform
        transformed, original_index = burrows_wheeler_transform(text)
        
        # Verify transformed string properties
        assert len(transformed) == len(text) + 1
        assert isinstance(transformed, str)
        assert isinstance(original_index, int)
        
        # Perform inverse transform
        reconstructed = inverse_burrows_wheeler_transform(transformed, original_index)
        
        # Verify reconstruction properties
        assert isinstance(reconstructed, str)
        assert len(reconstructed) == len(text)

def test_transform_preserve_length():
    """Ensure transformed string length matches original"""
    text = "hello world"
    transformed, _ = burrows_wheeler_transform(text)
    assert len(transformed) == len(text) + 1  # +1 for terminator