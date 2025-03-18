import json
from typing import Dict, List, Union, Optional
import os

class MultipleChoiceLogger:
    """
    A logger class for managing multiple-choice question responses.
    
    Provides functionality to log, retrieve, and manage user responses 
    to multiple-choice questions.
    """
    
    def __init__(self, log_file: str = 'responses.json'):
        """
        Initialize the MultipleChoiceLogger.
        
        Args:
            log_file (str, optional): Path to the JSON log file. 
                                      Defaults to 'responses.json'.
        """
        self.log_file = log_file
        self._ensure_log_file()
    
    def _ensure_log_file(self):
        """
        Ensure the log file exists, creating it if necessary.
        """
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)
    
    def log_response(self, 
                     question: str, 
                     response: str, 
                     user_id: Optional[str] = None) -> Dict[str, Union[str, None]]:
        """
        Log a user's response to a multiple-choice question.
        
        Args:
            question (str): The text of the multiple-choice question.
            response (str): The user's selected response.
            user_id (str, optional): Unique identifier for the user. Defaults to None.
        
        Returns:
            Dict containing logged response details.
        
        Raises:
            ValueError: If question or response is empty.
        """
        # Validate inputs
        if not question or not question.strip():
            raise ValueError("Question cannot be empty")
        
        if not response or not response.strip():
            raise ValueError("Response cannot be empty")
        
        # Read existing log
        with open(self.log_file, 'r') as f:
            log_entries = json.load(f)
        
        # Create new log entry
        log_entry = {
            "question": question.strip(),
            "response": response.strip(),
            "user_id": user_id,
            "timestamp": os.path.getmtime(self.log_file)
        }
        
        # Add entry to log
        log_entries.append(log_entry)
        
        # Write updated log
        with open(self.log_file, 'w') as f:
            json.dump(log_entries, f, indent=2)
        
        return log_entry
    
    def get_responses(self, 
                      user_id: Optional[str] = None) -> List[Dict[str, Union[str, None]]]:
        """
        Retrieve logged responses, optionally filtered by user ID.
        
        Args:
            user_id (str, optional): Filter responses by specific user. 
                                     Defaults to None (return all responses).
        
        Returns:
            List of response dictionaries.
        """
        with open(self.log_file, 'r') as f:
            log_entries = json.load(f)
        
        if user_id is not None:
            return [entry for entry in log_entries if entry['user_id'] == user_id]
        
        return log_entries
    
    def clear_log(self):
        """
        Clear all logged responses.
        """
        with open(self.log_file, 'w') as f:
            json.dump([], f)