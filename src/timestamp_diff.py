from datetime import datetime

def calculate_timestamp_difference(timestamp1: str, timestamp2: str, format: str = '%Y-%m-%d %H:%M:%S') -> float:
    """
    Calculate the time difference between two timestamps in seconds.

    Args:
        timestamp1 (str): First timestamp as a string
        timestamp2 (str): Second timestamp as a string
        format (str, optional): Format of the timestamps. Defaults to '%Y-%m-%d %H:%M:%S'

    Returns:
        float: Absolute time difference in seconds

    Raises:
        ValueError: If timestamps cannot be parsed with the given format
    """
    try:
        # Convert string timestamps to datetime objects
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)

        # Calculate absolute time difference in seconds
        return abs((dt2 - dt1).total_seconds())
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format. {str(e)}")