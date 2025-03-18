def stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for stable marriage problem.
    
    Args:
        men_preferences (list of lists): Preference lists for men, 
            where men_preferences[i] is man i's preference list
        women_preferences (list of lists): Preference lists for women, 
            where women_preferences[i] is woman i's preference list
    
    Returns:
        dict: A stable matching where keys are men and values are their matched women
    
    Raises:
        ValueError: If input lists are invalid or have unequal lengths
    """
    # Validate input
    if not men_preferences or not women_preferences:
        raise ValueError("Preference lists cannot be empty")
    
    n = len(men_preferences)
    if len(women_preferences) != n:
        raise ValueError("Men and women preference lists must have equal length")
    
    # Create preference rank dictionaries for faster lookup
    women_ranks = [
        {man: rank for rank, man in enumerate(pref)} 
        for pref in women_preferences
    ]
    
    # Initialize matching
    matching = {}  # men -> women
    women_partner = [None] * n  # women's current partners
    men_proposals = [0] * n  # tracks how many proposals each man has made
    
    # Continue while there are unmatched men
    while len(matching) < n:
        # Find an unmatched man
        unmatched_man = next(i for i in range(n) if i not in matching)
        
        # Get his top choice that he hasn't proposed to yet
        proposal_to = men_preferences[unmatched_man][men_proposals[unmatched_man]]
        men_proposals[unmatched_man] += 1
        
        # Check if woman is available or prefers new man
        if women_partner[proposal_to] is None:
            # Woman is free, match her
            matching[unmatched_man] = proposal_to
            women_partner[proposal_to] = unmatched_man
        else:
            # Woman is already matched, compare preferences
            current_partner = women_partner[proposal_to]
            
            # Check if she prefers new man
            if women_ranks[proposal_to][unmatched_man] < women_ranks[proposal_to][current_partner]:
                # New man is preferred, swap partners
                del matching[current_partner]
                matching[unmatched_man] = proposal_to
                women_partner[proposal_to] = unmatched_man
    
    return matching