def find_list_union(list1, list2):
    """
    Find the union of two lists, removing duplicates and maintaining order.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list containing unique elements from both input lists,
              preserving the order of first occurrence.

    Raises:
        TypeError: If either input is not a list.
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists")

    # Use an ordered set approach to maintain order and remove duplicates
    union_set = []
    seen = set()

    # Add elements from list1, preserving order
    for item in list1:
        if item not in seen:
            union_set.append(item)
            seen.add(item)

    # Add elements from list2 that are not already in the union
    for item in list2:
        if item not in seen:
            union_set.append(item)
            seen.add(item)

    return union_set