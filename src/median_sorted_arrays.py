def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays with O(log(min(m,n))) time complexity.
    
    Args:
        nums1 (List[int]): First sorted input array
        nums2 (List[int]): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input contains non-numeric elements
    """
    # Type checking
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise TypeError("Inputs must be lists")
    
    # Check for non-numeric elements
    if any(not isinstance(x, (int, float)) for x in nums1 + nums2):
        raise ValueError("Lists must contain only numeric elements")
    
    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    
    # Handle empty array cases
    if m == 0:
        # If one array is empty, median is from the other array
        mid = n // 2
        return nums2[mid] if n % 2 != 0 else (nums2[mid-1] + nums2[mid]) / 2
    
    # Binary search to partition the arrays
    low, high = 0, m
    
    while low <= high:
        # Partition both arrays
        partition_x = (low + high) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        # Find max and min values of partitions
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if partition is correct
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If total length is odd
            if (m + n) % 2 != 0:
                return max(max_left_x, max_left_y)
            
            # If total length is even
            return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
        
        # Adjust binary search
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1
    
    # If no valid partition found
    raise ValueError("Input arrays are not sorted")