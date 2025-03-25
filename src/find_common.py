def find_common(list1, list2):
    """
    Find and return a list of elements common to both input lists.

    Args:
        list1 (list): The first input list
        list2 (list): The second input list

    Returns:
        list: A list of elements that appear in both input lists

    Notes:
        - The function uses set intersection for efficient common element finding
        - Preserves order of first occurrence in list1
        - Works with lists of any hashable type
        - Returns an empty list if no common elements are found
    """
    # Convert lists to sets for efficient intersection
    set1 = set(list1)
    set2 = set(list2)

    # Find common elements while preserving order of first occurrence
    return [item for item in list1 if item in set2]