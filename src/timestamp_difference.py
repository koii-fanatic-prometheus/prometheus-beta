from datetime import datetime

def calculate_timestamp_difference(timestamp1: str, timestamp2: str, format: str = '%Y-%m-%d %H:%M:%S') -> float:
    """
    Calculate the time difference between two timestamps in seconds.

    Args:
        timestamp1 (str): First timestamp string
        timestamp2 (str): Second timestamp string
        format (str, optional): Datetime format string. Defaults to '%Y-%m-%d %H:%M:%S'.

    Returns:
        float: Time difference in seconds. Positive if timestamp2 is later than timestamp1.

    Raises:
        ValueError: If timestamps cannot be parsed using the given format
    """
    try:
        # Parse the timestamps using the specified format
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)

        # Calculate the time difference and return seconds
        return (dt2 - dt1).total_seconds()
    except ValueError as e:
        # Raise a more descriptive error if parsing fails
        raise ValueError(f"Error parsing timestamps: {e}. Ensure timestamps match the format {format}")