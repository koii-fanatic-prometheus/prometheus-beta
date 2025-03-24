import pytest
import random
from src.array_shuffle import shuffle_array

class TestArrayShuffle:
    def test_shuffle_basic_list(self):
        """Test shuffling a basic list of integers"""
        original = [1, 2, 3, 4, 5]
        shuffled = shuffle_array(original)
        
        # Verify that shuffled list contains same elements
        assert set(shuffled) == set(original)
        
        # Verify that the order is different (with high probability)
        assert shuffled != original

    def test_shuffle_empty_list(self):
        """Test shuffling an empty list"""
        assert shuffle_array([]) == []

    def test_shuffle_single_element_list(self):
        """Test shuffling a list with a single element"""
        single_list = [42]
        assert shuffle_array(single_list) == single_list

    def test_shuffle_different_types(self):
        """Test shuffling a list with different types of elements"""
        mixed_list = [1, 'a', True, 3.14, None]
        shuffled = shuffle_array(mixed_list)
        
        # Verify that shuffled list contains same elements
        assert set(shuffled) == set(mixed_list)
        
        # Verify that the order is different (with high probability)
        assert shuffled != mixed_list

    def test_shuffle_not_modifying_original(self):
        """Verify that the original list is not modified"""
        original = [1, 2, 3, 4, 5]
        shuffled = shuffle_array(original)
        
        assert original == [1, 2, 3, 4, 5]  # Original list unchanged
        assert len(shuffled) == len(original)

    def test_shuffle_randomness(self):
        """Test that multiple shuffles produce different orders"""
        original = list(range(10))
        
        # Set a fixed seed for reproducibility of randomness check
        random.seed(42)
        
        # Perform multiple shuffles
        shuffles = [shuffle_array(original) for _ in range(5)]
        
        # Check that not all shuffles are the same
        assert len(set(tuple(shuffle) for shuffle in shuffles)) > 1

    def test_invalid_input_type(self):
        """Test that non-list inputs raise TypeError"""
        with pytest.raises(TypeError):
            shuffle_array("not a list")
        
        with pytest.raises(TypeError):
            shuffle_array(42)
        
        with pytest.raises(TypeError):
            shuffle_array(None)