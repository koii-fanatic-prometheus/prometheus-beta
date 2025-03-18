import os
import json
import pytest
import time
from src.multiple_choice_logger import MultipleChoiceLogger

@pytest.fixture
def temp_log_file(tmp_path):
    """Fixture to create a temporary log file for each test."""
    log_file = tmp_path / "test_responses.json"
    return str(log_file)

def test_logger_initialization(temp_log_file):
    """Test that the logger creates a log file if it doesn't exist."""
    logger = MultipleChoiceLogger(log_file=temp_log_file)
    assert os.path.exists(temp_log_file)
    
    # Check that the file contains an empty list
    with open(temp_log_file, 'r') as f:
        log_entries = json.load(f)
    assert log_entries == []

def test_log_response(temp_log_file):
    """Test logging a single response."""
    logger = MultipleChoiceLogger(log_file=temp_log_file)
    
    response = logger.log_response("What is the capital of France?", "Paris", "user1")
    
    # Verify response details
    assert response['question'] == "What is the capital of France?"
    assert response['response'] == "Paris"
    assert response['user_id'] == "user1"
    assert 'timestamp' in response

    # Verify log file contents
    with open(temp_log_file, 'r') as f:
        log_entries = json.load(f)
    assert len(log_entries) == 1
    assert log_entries[0] == response

def test_log_multiple_responses(temp_log_file):
    """Test logging multiple responses."""
    logger = MultipleChoiceLogger(log_file=temp_log_file)
    
    # Log multiple responses
    logger.log_response("Q1", "A1", "user1")
    logger.log_response("Q2", "A2", "user2")
    
    # Retrieve and verify responses
    responses = logger.get_responses()
    assert len(responses) == 2
    assert responses[0]['question'] == "Q1"
    assert responses[1]['question'] == "Q2"

def test_get_responses_by_user(temp_log_file):
    """Test retrieving responses for a specific user."""
    logger = MultipleChoiceLogger(log_file=temp_log_file)
    
    # Log responses for different users
    logger.log_response("Q1", "A1", "user1")
    logger.log_response("Q2", "A2", "user2")
    logger.log_response("Q3", "A3", "user1")
    
    # Retrieve user1's responses
    user1_responses = logger.get_responses("user1")
    assert len(user1_responses) == 2
    assert all(resp['user_id'] == "user1" for resp in user1_responses)

def test_invalid_response_inputs(temp_log_file):
    """Test error handling for invalid inputs."""
    logger = MultipleChoiceLogger(log_file=temp_log_file)
    
    # Test empty question
    with pytest.raises(ValueError, match="Question cannot be empty"):
        logger.log_response("", "Response", "user1")
    
    # Test empty response
    with pytest.raises(ValueError, match="Response cannot be empty"):
        logger.log_response("Question", "", "user1")

def test_clear_log(temp_log_file):
    """Test clearing the log."""
    logger = MultipleChoiceLogger(log_file=temp_log_file)
    
    # Log some responses
    logger.log_response("Q1", "A1", "user1")
    logger.log_response("Q2", "A2", "user2")
    
    # Clear the log
    logger.clear_log()
    
    # Verify log is empty
    responses = logger.get_responses()
    assert len(responses) == 0

def test_optional_user_id(temp_log_file):
    """Test logging with optional user ID."""
    logger = MultipleChoiceLogger(log_file=temp_log_file)
    
    # Log response without user ID
    response = logger.log_response("Q1", "A1")
    assert response['user_id'] is None
    
    # Retrieve responses
    responses = logger.get_responses()
    assert len(responses) == 1