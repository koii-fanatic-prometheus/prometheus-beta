def remove_duplicates_and_sort(arr):
    """
    Remove duplicate elements from an array and sort in ascending order 
    without using built-in sorting or duplicate removal methods.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed and sorted in ascending order
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Remove duplicates using a simple approach
    unique_nums = []
    for num in arr:
        if num not in unique_nums:
            unique_nums.append(num)
    
    # Custom bubble sort to sort the unique numbers
    for i in range(len(unique_nums)):
        for j in range(0, len(unique_nums) - i - 1):
            if unique_nums[j] > unique_nums[j + 1]:
                # Swap elements
                unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]
    
    return unique_nums