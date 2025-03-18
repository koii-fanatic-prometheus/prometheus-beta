import pytest
from src.stable_marriage import stable_marriage

def test_basic_stable_marriage():
    """Test a simple stable marriage scenario"""
    men_preferences = [
        [0, 1],  # Man 0's preferences
        [1, 0]   # Man 1's preferences
    ]
    women_preferences = [
        [1, 0],  # Woman 0's preferences
        [0, 1]   # Woman 1's preferences
    ]
    
    matching = stable_marriage(men_preferences, women_preferences)
    
    # Verify matching
    assert len(matching) == 2
    assert matching[0] == 0 or matching[0] == 1
    assert matching[1] == 0 or matching[1] == 1
    assert matching[0] != matching[1]

def test_larger_stable_marriage():
    """Test a more complex stable marriage scenario"""
    men_preferences = [
        [0, 1, 2],  # Man 0's preferences
        [1, 2, 0],  # Man 1's preferences
        [2, 0, 1]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 2, 0],  # Woman 0's preferences 
        [2, 0, 1],  # Woman 1's preferences
        [0, 1, 2]   # Woman 2's preferences
    ]
    
    matching = stable_marriage(men_preferences, women_preferences)
    
    # Verify matching
    assert len(matching) == 3
    
    # Verify each man is matched to a unique woman
    assert len(set(matching.values())) == 3

def test_empty_input_error():
    """Test handling of empty input lists"""
    with pytest.raises(ValueError, match="Preference lists cannot be empty"):
        stable_marriage([], [])

def test_unequal_length_error():
    """Test handling of unequal length preference lists"""
    men_preferences = [[0, 1], [1, 0]]
    women_preferences = [[0], [1], [2]]
    
    with pytest.raises(ValueError, match="Men and women preference lists must have equal length"):
        stable_marriage(men_preferences, women_preferences)

def test_stability_property():
    """Verify the stability of the matching"""
    men_preferences = [
        [0, 1, 2],  # Man 0's preferences
        [1, 2, 0],  # Man 1's preferences
        [2, 0, 1]   # Man 2's preferences
    ]
    women_preferences = [
        [1, 2, 0],  # Woman 0's preferences 
        [2, 0, 1],  # Woman 1's preferences
        [0, 1, 2]   # Woman 2's preferences
    ]
    
    matching = stable_marriage(men_preferences, women_preferences)
    
    # Check stability
    for man, woman in matching.items():
        # Check if any man prefers another woman over his match
        for preferred_woman in men_preferences[man]:
            if preferred_woman == woman:
                break
            
            # Find her current partner
            current_partner = None
            for m, w in matching.items():
                if w == preferred_woman:
                    current_partner = m
                    break
            
            # Check if she prefers the current man to the proposed man
            if current_partner is not None:
                women_pref = women_preferences[preferred_woman]
                assert women_pref.index(current_partner) < women_pref.index(man), \
                    f"Unstable match: Man {man} could break match with Woman {woman}"