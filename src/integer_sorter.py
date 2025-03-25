def merge_sort(arr):
    """
    Sort an array of integers in non-decreasing order using merge sort algorithm.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A new sorted list in non-decreasing order.
    
    Raises:
        TypeError: If input is not a list.
        TypeError: If list contains non-integer elements.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Base case: if list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Recursive merge sort implementation
    def merge(left, right):
        """Merge two sorted lists into a single sorted list."""
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements from left or right list
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)