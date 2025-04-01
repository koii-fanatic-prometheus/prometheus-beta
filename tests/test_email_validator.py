import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats"""
    valid_emails = [
        'user@example.com',
        'john.doe@example.co.uk',
        'user123@domain.org',
        'user+tag@example.com',
        'first.last@domain.name',
        'user@domain-name.com'
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats"""
    invalid_emails = [
        '',                     # Empty string
        'invalid-email',        # No @ symbol
        'user@.com',            # Invalid domain
        '@domain.com',          # Missing local part
        'user@domain',          # Missing top-level domain
        'user@@domain.com',     # Multiple @ symbols
        'user@domain..com',     # Consecutive dots
        'user@domain.c',        # Top-level domain too short
        ' user@domain.com',     # Leading space
        'user@domain.com ',     # Trailing space
        None,                   # None input
        123,                    # Non-string input
        'very' + 'long' * 50 + '@domain.com'  # Too long email
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email formats"""
    edge_case_emails = [
        'a@b.co',               # Minimal valid email
        'user+tag+another@example.com',  # Multiple + in local part
        'user.name+tag@very-long-domain-name.com'
    ]
    for email in edge_case_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_unicode_and_special_chars():
    """Test email validation with special characters (should mostly be invalid)"""
    special_emails = [
        'user name@domain.com',  # Space in local part
        'user@domain name.com',  # Space in domain
        'user🚀@domain.com',     # Emoji in local part
        'üser@domain.com',       # Unicode character
    ]
    for email in special_emails:
        assert validate_email(email) is False, f"{email} should be invalid"