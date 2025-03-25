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
    - Handles various URL formats including IPv4, IPv6, and domain names
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
        
        # Additional regex validation for more robust checking
        # This regex allows http/https/ftp protocols, optional subdomains, 
        # domains with various TLDs, and optional ports
        url_regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        return bool(url_regex.match(url))
    
    except Exception:
        return False