def reverse_string_in_place(s: list) -> None:
    """
    Reverse a string in-place without creating a new string.
    
    This function modifies the input list of characters in-place,
    reversing their order with O(1) extra space complexity.
    
    Args:
        s (list): A list of characters to be reversed in-place.
    
    Time Complexity: O(n), where n is the length of the string
    Space Complexity: O(1), as reversal is done in-place
    
    Raises:
        TypeError: If input is not a list
    
    Example:
        >>> chars = list('hello')
        >>> reverse_string_in_place(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']
    """
    # Check input type
    if not isinstance(s, list):
        raise TypeError("Input must be a list of characters")
    
    # Two-pointer approach for in-place reversal
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards center
        left += 1
        right -= 1