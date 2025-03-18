import pytest
from src.alternating_dot_case import to_alternating_dot_case

def test_basic_string():
    """Test conversion of a basic string."""
    assert to_alternating_dot_case("hello") == 'h.e.l.l.o'

def test_multiple_words():
    """Test conversion of a multi-word string."""
    assert to_alternating_dot_case("hello world") == 'h.e.l.l.o. .w.o.r.l.d'

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_dot_case("") == ''

def test_single_character():
    """Test conversion of a single character."""
    assert to_alternating_dot_case("a") == 'a'

def test_mixed_case():
    """Test conversion of a mixed case string."""
    assert to_alternating_dot_case("PytHon") == 'P.y.t.H.o.n'

def test_non_string_input():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_dot_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_dot_case(None)

def test_special_characters():
    """Test conversion with special characters."""
    assert to_alternating_dot_case("hello!@#") == 'h.e.l.l.o.!.@.#'