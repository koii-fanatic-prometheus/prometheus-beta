from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.

    Args:
        date (str or datetime): The input date to add days to.
            Accepts date strings in 'YYYY-MM-DD' format or datetime objects.
        days (int): Number of days to add. Can be positive or negative.

    Returns:
        datetime: A new datetime object representing the date after adding the specified days.

    Raises:
        ValueError: If the input date is invalid or cannot be parsed.
        TypeError: If days is not an integer.
    """
    # Validate input types
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")

    # Handle string input by converting to datetime
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")

    # Validate that date is a datetime object
    if not isinstance(date, datetime):
        raise TypeError("Date must be a string in 'YYYY-MM-DD' format or a datetime object")

    # Add days and return new datetime
    return date + timedelta(days=days)