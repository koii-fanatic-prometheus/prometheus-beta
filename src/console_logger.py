def log_message(message):
    """
    Log a simple message to the console.

    Args:
        message (str): The message to be logged.

    Raises:
        TypeError: If the message is not a string.
    """
    # Validate input is a string
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # Print the message to the console
    print(message)