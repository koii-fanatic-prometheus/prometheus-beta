import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.

    Validation criteria:
    - Must have a local part (before @)
    - Must have a domain part (after @)
    - Local part can contain letters, digits, and some special characters
    - Domain must have at least one dot
    - Total length should not exceed 254 characters
    - Follows common email format rules
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False

    # Check total length (RFC 5321 specifies max 254 characters)
    if len(email) > 254:
        return False

    # Regular expression for email validation
    # Follows most common email format rules
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Additional checks:
    # 1. Ensure no consecutive dots in local or domain part
    # 2. Ensure domain has at least one dot
    # 3. Ensure local part and domain are not too long
    if (re.match(email_regex, email) and 
        '..' not in email and 
        len(email.split('@')[0]) <= 64 and  # Local part max length
        len(email.split('@')[1]) <= 255):   # Domain part max length
        return True
    
    return False