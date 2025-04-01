from termcolor import colored

def log_colored_message(message, color='green', attrs=None):
    """
    Log a message in a specified color.

    Args:
        message (str): The message to log.
        color (str, optional): Color of the message. 
            Defaults to 'green'. 
            Supported colors: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
        attrs (list, optional): Text attributes like 'bold', 'underline', etc.
            Defaults to None.

    Raises:
        TypeError: If message is not a string.
        ValueError: If an unsupported color is provided.

    Returns:
        str: The colored message.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Validate color
    supported_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    if color not in supported_colors:
        raise ValueError(f"Unsupported color. Choose from {supported_colors}")

    # Default to no attributes if None
    if attrs is None:
        attrs = []

    # Color the message
    return colored(message, color, attrs=attrs)