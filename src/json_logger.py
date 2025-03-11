import json
import logging

def log_json(logger, level, json_obj, message=None):
    """
    Log a JSON object with proper formatting and optional custom message.

    Args:
        logger (logging.Logger): The logger instance to use for logging.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        json_obj (dict): The JSON object to log.
        message (str, optional): Custom message to prepend to the JSON log.

    Raises:
        TypeError: If json_obj is not a dictionary.
        ValueError: If level is not a valid logging level.

    Returns:
        None
    """
    # Validate inputs
    if not isinstance(json_obj, dict):
        raise TypeError("json_obj must be a dictionary.")
    
    # Validate logging level
    valid_levels = [logging.DEBUG, logging.INFO, logging.WARNING, 
                    logging.ERROR, logging.CRITICAL]
    if level not in valid_levels:
        raise ValueError(f"Invalid logging level. Must be one of {valid_levels}")

    # Use hasattr to check for 'log' method instead of isinstance
    if not hasattr(logger, 'log'):
        raise TypeError("Invalid logger. Must have a 'log' method.")

    # Format JSON with proper indentation
    try:
        formatted_json = json.dumps(json_obj, indent=2)
    except TypeError:
        raise TypeError("JSON object contains non-serializable elements.")

    # Prepare log message
    log_message = formatted_json if message is None else f"{message}\n{formatted_json}"

    # Log the message at the specified level
    logger.log(level, log_message)