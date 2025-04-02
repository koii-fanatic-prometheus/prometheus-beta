import readline
import logging
from typing import Optional, Callable

class ReadlineLogger:
    """
    A utility class for logging interactive prompts using readline.
    
    This class provides methods to log user inputs and handle readline interactions
    with robust error handling and logging capabilities.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the ReadlineLogger.
        
        Args:
            logger (Optional[logging.Logger]): A logger instance. 
                If not provided, a default logger will be created.
        """
        self.logger = logger or logging.getLogger(__name__)
    
    def log_input(self, prompt: str, 
                  input_validator: Optional[Callable[[str], bool]] = None,
                  max_attempts: int = 3) -> Optional[str]:
        """
        Interactively log user input with optional validation.
        
        Args:
            prompt (str): The prompt to display to the user.
            input_validator (Optional[Callable[[str], bool]]): Optional function 
                to validate input. Returns True if input is valid.
            max_attempts (int): Maximum number of input attempts. Defaults to 3.
        
        Returns:
            Optional[str]: The validated input, or None if max attempts exceeded.
        
        Raises:
            TypeError: If prompt is not a string.
            ValueError: If max_attempts is less than 1.
        """
        # Validate input parameters
        if not isinstance(prompt, str):
            raise TypeError("Prompt must be a string")
        
        if max_attempts < 1:
            raise ValueError("Max attempts must be at least 1")
        
        # Log the initial prompt
        self.logger.info(f"Prompting user: {prompt}")
        
        for attempt in range(1, max_attempts + 1):
            try:
                # Use readline for input with the given prompt
                user_input = input(prompt)
                
                # If no validator is provided, return the input
                if input_validator is None:
                    self.logger.info("Input received successfully")
                    return user_input
                
                # Validate input if a validator is provided
                if input_validator(user_input):
                    self.logger.info("Input validated successfully")
                    return user_input
                
                # Log validation failure
                self.logger.warning(f"Input validation failed (Attempt {attempt})")
                print(f"Invalid input. Please try again. (Attempt {attempt}/{max_attempts})")
            
            except KeyboardInterrupt:
                # Handle interrupt gracefully
                self.logger.warning("Input interrupted by user")
                print("\nInput interrupted. Exiting.")
                return None
            except Exception as e:
                # Log any unexpected errors
                self.logger.error(f"Unexpected error during input: {e}")
                print(f"An error occurred: {e}")
        
        # Exceeded max attempts
        self.logger.error("Exceeded maximum input attempts")
        print("Maximum attempts reached. Input cancelled.")
        return None