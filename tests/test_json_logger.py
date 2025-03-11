import logging
import pytest
from src.json_logger import log_json

# Custom logger for testing
class MockLogger:
    def __init__(self):
        self.logged_messages = []
        self.last_level = None

    def log(self, level, message):
        self.logged_messages.append(message)
        self.last_level = level

def test_log_json_without_message():
    mock_logger = MockLogger()
    test_obj = {"key1": "value1", "key2": 42}
    
    log_json(mock_logger, logging.INFO, test_obj)
    
    assert len(mock_logger.logged_messages) == 1
    assert '"key1": "value1"' in mock_logger.logged_messages[0]
    assert '"key2": 42' in mock_logger.logged_messages[0]
    assert mock_logger.last_level == logging.INFO

def test_log_json_with_message():
    mock_logger = MockLogger()
    test_obj = {"key1": "value1", "key2": 42}
    
    log_json(mock_logger, logging.DEBUG, test_obj, "Test message")
    
    assert len(mock_logger.logged_messages) == 1
    assert "Test message" in mock_logger.logged_messages[0]
    assert '"key1": "value1"' in mock_logger.logged_messages[0]
    assert mock_logger.last_level == logging.DEBUG

def test_invalid_logger():
    with pytest.raises(TypeError, match="Invalid logger"):
        log_json("not a logger", logging.INFO, {})

def test_invalid_json_obj():
    mock_logger = MockLogger()
    with pytest.raises(TypeError, match="json_obj must be a dictionary"):
        log_json(mock_logger, logging.INFO, "not a dict")

def test_invalid_logging_level():
    mock_logger = MockLogger()
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_json(mock_logger, 999, {})

def test_non_serializable_json():
    mock_logger = MockLogger()
    non_serializable = {"func": lambda x: x}
    
    with pytest.raises(TypeError, match="non-serializable elements"):
        log_json(mock_logger, logging.INFO, non_serializable)

def test_nested_json():
    mock_logger = MockLogger()
    nested_obj = {
        "user": {
            "name": "John",
            "age": 30,
            "address": {
                "city": "New York",
                "zip": "10001"
            }
        }
    }
    
    log_json(mock_logger, logging.INFO, nested_obj)
    
    assert len(mock_logger.logged_messages) == 1
    logged_msg = mock_logger.logged_messages[0]
    assert '"name": "John"' in logged_msg
    assert '"city": "New York"' in logged_msg
    assert mock_logger.last_level == logging.INFO