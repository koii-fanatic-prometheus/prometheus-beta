import pytest
from src.burrows_wheeler_transform import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_basic():
    """Test basic Burrows-Wheeler Transform functionality"""
    text = "banana"
    transformed, original_index = burrows_wheeler_transform(text)
    assert isinstance(transformed, str)
    assert isinstance(original_index, int)
    
    # Note: We expect the dollar sign to be included in the reconstruction
    reconstructed = inverse_burrows_wheeler_transform(transformed, original_index)
    assert reconstructed.rstrip('$') == text

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

def test_burrows_wheeler_transform_complex_string():
    """Test transform with a more complex string"""
    text = "ABRACADABRA"
    transformed, original_index = burrows_wheeler_transform(text)
    reconstructed = inverse_burrows_wheeler_transform(transformed, original_index)
    assert reconstructed.rstrip('$') == text

def test_burrows_wheeler_transform_repeated_chars():
    """Test transform with repeated characters"""
    text = "MISSISSIPPI"
    transformed, original_index = burrows_wheeler_transform(text)
    reconstructed = inverse_burrows_wheeler_transform(transformed, original_index)
    assert reconstructed.rstrip('$') == text

def test_transform_preserve_length():
    """Ensure transformed string length matches original"""
    text = "hello world"
    transformed, _ = burrows_wheeler_transform(text)
    assert len(transformed) == len(text) + 1  # +1 for terminator

def test_multiple_transforms():
    """Test multiple successive transforms"""
    test_strings = ["banana", "ABRACADABRA", "hello world", "python"]
    
    for text in test_strings:
        transformed, original_index = burrows_wheeler_transform(text)
        reconstructed = inverse_burrows_wheeler_transform(transformed, original_index)
        assert reconstructed.rstrip('$') == text