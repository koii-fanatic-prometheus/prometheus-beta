def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of digits representing numbers.

    Args:
        A (list): First array of digits representing a number
        B (list): Second array of digits representing a number

    Returns:
        list: Array of digits representing the product of the two input numbers

    Raises:
        ValueError: If input arrays are empty or of different lengths
        TypeError: If inputs contain non-integer elements
    """
    # Input validation
    if not A or not B:
        raise ValueError("Input arrays cannot be empty")
    
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) and 0 <= x <= 9 for x in A + B):
        raise TypeError("All elements must be integers between 0 and 9")
    
    # Convert digit arrays to integers
    num1 = int(''.join(map(str, A)))
    num2 = int(''.join(map(str, B)))
    
    # Multiply and convert back to digit array
    product = num1 * num2
    
    # Convert product to list of digits
    return [int(digit) for digit in str(product)]