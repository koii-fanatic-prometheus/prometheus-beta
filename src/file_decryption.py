import os
from cryptography.fernet import Fernet

def decrypt_file(input_path, output_path, key):
    """
    Decrypt an encrypted file using Fernet symmetric encryption.

    Args:
        input_path (str): Path to the encrypted input file
        output_path (str): Path where the decrypted file will be saved
        key (bytes): The encryption key used for decryption

    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
        ValueError: If the key is invalid or decryption fails
    """
    try:
        # Validate inputs
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        if not isinstance(key, bytes):
            raise ValueError("Encryption key must be bytes")

        # Create Fernet cipher using the key
        fernet = Fernet(key)

        # Read encrypted file
        with open(input_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Decrypt the file content
        try:
            decrypted_data = fernet.decrypt(encrypted_data)
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")

        # Write decrypted data to output file
        with open(output_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        return True
    except Exception as e:
        raise