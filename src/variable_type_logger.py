import logging

def log_variable_type(variable):
    """
    Log the type of a given variable.

    Args:
        variable: Any Python variable to log the type of.

    Returns:
        str: The string representation of the variable's type.

    Notes:
        - Uses Python's built-in type() function to determine the type
        - Logs the type at INFO level
        - Can handle any type of variable (int, str, list, dict, etc.)
    """
    # Get the type of the variable as a string
    var_type = type(variable).__name__
    
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Log the type of the variable
    logging.info(f"Variable type: {var_type}")
    
    return var_type