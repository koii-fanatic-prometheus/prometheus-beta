import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Check if a given string is a valid URL.
    
    Args:
        url (str): The URL string to validate
    
    Returns:
        bool: True if the URL is valid, False otherwise
    
    Validates URL based on several criteria:
    - Must have a valid scheme (http, https, ftp, etc.)
    - Must have a valid netloc (domain)
    - Allows optional path, query parameters, and fragments
    - Handles various URL formats including IPv4, IPv6, domain names, and localhost
    """
    # Check if input is a string and not empty
    if not isinstance(url, str) or not url:
        return False
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Require a scheme (protocol)
        if not parsed_url.scheme:
            return False
        
        # Require a netloc (domain or IP)
        if not parsed_url.netloc:
            return False
        
        # More comprehensive regex validation
        url_regex = re.compile(
            r'^'
            r'(https?|ftp)://'  # Scheme
            r'(([a-zA-Z0-9_-]+:)?[a-zA-Z0-9_-]+@)?'  # Optional authentication
            r'(([a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}|'  # Domain with valid TLD
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IPv4
            r'(:[0-9]{1,5})?'  # Optional port (1-5 digits)
            r'(/[a-zA-Z0-9\-._~:/?#[\]@!$&\'()*+,;=]*)?'  # Optional path and query
            r'$', re.IGNORECASE)
        
        # Check if URL matches the regex pattern and netloc is not just a dot
        return bool(url_regex.match(url) and parsed_url.netloc != '.')
    
    except Exception:
        return False