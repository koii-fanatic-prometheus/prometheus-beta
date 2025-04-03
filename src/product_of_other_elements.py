def product_of_other_elements(nums):
    """
    Returns a list where each element is the product of all other elements except itself.
    
    Args:
        nums (list): Input list of integers
    
    Returns:
        list: A list where each element is the product of all other elements except the element at that index
    
    Raises:
        ValueError: If input is not a list
        TypeError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(nums, list):
        raise ValueError("Input must be a list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in nums):
        raise TypeError("All list elements must be numeric")
    
    # Handle empty list or single-element list
    if len(nums) <= 1:
        return [1] * len(nums)
    
    # Calculate total product first
    total_product = 1
    for num in nums:
        total_product *= num
    
    # Create result list by dividing total product by each element
    result = []
    for num in nums:
        # Avoid division by zero
        if num == 0:
            # If this is the only zero, product will be total product of non-zero elements
            # If multiple zeros, product will be zero
            zero_count = nums.count(0)
            if zero_count > 1:
                result.append(0)
            else:
                # Calculate product of all non-zero elements
                non_zero_product = 1
                for x in nums:
                    if x != 0:
                        non_zero_product *= x
                result.append(non_zero_product)
        else:
            result.append(total_product // num)
    
    return result