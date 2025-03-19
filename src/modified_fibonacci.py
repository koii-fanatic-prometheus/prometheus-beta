def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence up to a given number where 
    the sum of any two consecutive numbers (starting from the third) 
    is always divisible by 3.

    Args:
        n (int): The maximum number in the Fibonacci sequence.

    Returns:
        list: A modified Fibonacci sequence.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Handle edge cases
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    # Initialize the sequence
    sequence = [1, 1]

    # Generate the modified Fibonacci sequence
    while sequence[-1] <= n:
        # Calculate the next number that ensures the constraint
        next_num = sequence[-1] + sequence[-2]
        
        # Adjust the next number if needed to satisfy the divisibility constraint
        while (sequence[-1] + sequence[-2]) % 3 != 0:
            next_num += 1
        
        # Stop if the next number exceeds the input
        if next_num > n:
            break
        
        sequence.append(next_num)

    return sequence