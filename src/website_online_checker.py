import requests

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online by attempting to connect to it.

    Args:
        url (str): The full URL of the website to check (including protocol, e.g., 'https://www.example.com')
        timeout (float, optional): Number of seconds to wait for a response. Defaults to 5.0 seconds.

    Returns:
        bool: True if the website is online and responds with a successful status code, False otherwise.

    Raises:
        ValueError: If the URL is invalid or empty.
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")

    # Ensure URL starts with a protocol
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'

    try:
        # Send a HEAD request to check if the website is online
        response = requests.head(url, timeout=timeout)
        
        # Consider status codes in the 200-299 range as successful
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # Any connection or request errors indicate the website is not online
        return False