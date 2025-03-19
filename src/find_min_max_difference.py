def find_min_max_difference(numbers_str):
    """
    Calculate the difference between the largest and smallest numbers in a 
    comma-separated string of integers.

    Args:
        numbers_str (str): A string of comma-separated integers.

    Returns:
        int: The difference between the largest and smallest numbers.

    Raises:
        ValueError: If the input string is empty or contains non-integer values.
    """
    # Check for empty string
    if not numbers_str:
        raise ValueError("Input string cannot be empty")

    # Split the string and convert to integers, filtering out empty strings
    try:
        numbers = [int(num.strip()) for num in numbers_str.split(',') if num.strip()]
    except ValueError:
        raise ValueError("Input must be a string of comma-separated integers")

    # Check if the list is empty 
    if not numbers:
        raise ValueError("No valid integers found in the input string")

    # Return the difference between max and min
    return max(numbers) - min(numbers)