import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    # Test various valid URL formats
    valid_urls = [
        "http://www.example.com",
        "https://example.com",
        "https://www.example.co.uk",
        "http://localhost",
        "https://localhost:8000",
        "http://192.168.1.1",
        "https://192.168.1.1:8080",
        "ftp://files.example.com",
        "https://example.com/path",
        "https://example.com/path?param=value",
        "https://example.com/path#fragment"
    ]
    
    for url in valid_urls:
        assert is_valid_url(url), f"{url} should be valid"

def test_invalid_urls():
    # Test various invalid URL formats
    invalid_urls = [
        "",  # Empty string
        "not a url",
        "www.example.com",  # Missing scheme
        "http://",  # Incomplete URL
        "https:// ",  # Whitespace
        None,  # None value
        "://example.com",  # Invalid scheme
        "http://.",  # Invalid domain
        "https://example",  # Incomplete domain
    ]
    
    for url in invalid_urls:
        assert not is_valid_url(url), f"{url} should be invalid"

def test_edge_cases():
    # Test some tricky edge cases
    edge_case_urls = [
        "http://example.com:65535",  # Max port number
        "https://sub.domain.example.co.uk/path?param=value#fragment",
        "ftp://user:pass@example.com"
    ]
    
    for url in edge_case_urls:
        assert is_valid_url(url), f"{url} should be valid"

def test_input_types():
    # Test various input types
    assert not is_valid_url(123)  # Integer
    assert not is_valid_url(None)  # None
    assert not is_valid_url([])  # List
    assert not is_valid_url({})  # Dictionary