import pytest
import requests
from src.website_online_checker import is_website_online

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

def test_is_website_online_valid_website(monkeypatch):
    """Test that a valid, online website returns True"""
    def mock_head(*args, **kwargs):
        return MockResponse(200)
    
    monkeypatch.setattr(requests, 'head', mock_head)
    
    assert is_website_online('https://www.example.com') is True

def test_is_website_online_offline_website(monkeypatch):
    """Test that an offline website returns False"""
    def mock_head(*args, **kwargs):
        raise requests.ConnectionError()
    
    monkeypatch.setattr(requests, 'head', mock_head)
    
    assert is_website_online('https://www.nonexistentwebsite123456.com') is False

def test_is_website_online_timeout(monkeypatch):
    """Test that a website that times out returns False"""
    def mock_head(*args, **kwargs):
        raise requests.Timeout()
    
    monkeypatch.setattr(requests, 'head', mock_head)
    
    assert is_website_online('https://www.slowwebsite.com', timeout=1.0) is False

def test_is_website_online_empty_url():
    """Test that an empty URL raises a ValueError"""
    with pytest.raises(ValueError):
        is_website_online('')

def test_is_website_online_none_url():
    """Test that None raises a ValueError"""
    with pytest.raises(ValueError):
        is_website_online(None)

def test_is_website_online_without_protocol(monkeypatch):
    """Test that URLs without a protocol are handled correctly"""
    def mock_head(url, *args, **kwargs):
        assert url.startswith('https://')
        return MockResponse(200)
    
    monkeypatch.setattr(requests, 'head', mock_head)
    
    assert is_website_online('example.com') is True

def test_is_website_online_redirect(monkeypatch):
    """Test that a redirected website (3xx status) is considered online"""
    def mock_head(*args, **kwargs):
        return MockResponse(302)  # Redirect status
    
    monkeypatch.setattr(requests, 'head', mock_head)
    
    assert is_website_online('https://www.redirectedsite.com') is True

def test_is_website_online_server_error(monkeypatch):
    """Test that server errors return False"""
    def mock_head(*args, **kwargs):
        return MockResponse(500)
    
    monkeypatch.setattr(requests, 'head', mock_head)
    
    assert is_website_online('https://www.servererror.com') is False