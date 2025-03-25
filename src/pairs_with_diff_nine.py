def find_sum_of_pairs_with_diff_nine(file_path):
    """
    Read numbers from a text file and return the sum of all pairs 
    of numbers that have a difference of exactly 9.

    Args:
        file_path (str): Path to the text file containing numbers.
    
    Returns:
        int: Sum of all pairs of numbers with a difference of 9.
    
    Raises:
        FileNotFoundError: If the specified file cannot be found.
        ValueError: If the file contains non-numeric content.
    """
    try:
        # Read numbers from the file
        with open(file_path, 'r') as file:
            # Convert file contents to list of integers
            numbers = [int(line.strip()) for line in file if line.strip()]
        
        # Track the sum of pairs
        total_sum = 0
        
        # Create a set for O(1) lookup
        number_set = set(numbers)
        
        # Find pairs with difference of 9
        for num in numbers:
            # Check both num + 9 and num - 9
            if num + 9 in number_set:
                total_sum += num + (num + 9)
            elif num - 9 in number_set:
                total_sum += num + (num - 9)
        
        # Divide by 2 to avoid counting each pair twice
        return total_sum // 2
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError(f"Invalid numeric content in file: {file_path}")