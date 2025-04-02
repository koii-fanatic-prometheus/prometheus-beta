import os
import pytest
from cryptography.fernet import Fernet
from src.file_decryption import decrypt_file

@pytest.fixture
def encryption_key():
    return Fernet.generate_key()

@pytest.fixture
def sample_encrypted_file(tmp_path, encryption_key):
    # Create a sample file to encrypt
    input_file = tmp_path / "sample.txt"
    encrypted_file = tmp_path / "encrypted.bin"
    decrypted_file = tmp_path / "decrypted.txt"
    
    input_file.write_text("This is a secret message!")
    
    # Encrypt the file
    fernet = Fernet(encryption_key)
    with open(input_file, 'rb') as f:
        file_data = f.read()
    encrypted_data = fernet.encrypt(file_data)
    
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_data)
    
    return {
        'input_file': str(input_file),
        'encrypted_file': str(encrypted_file),
        'decrypted_file': str(decrypted_file),
        'key': encryption_key
    }

def test_successful_decryption(sample_encrypted_file):
    result = decrypt_file(
        sample_encrypted_file['encrypted_file'], 
        sample_encrypted_file['decrypted_file'], 
        sample_encrypted_file['key']
    )
    
    assert result is True
    with open(sample_encrypted_file['decrypted_file'], 'r') as f:
        decrypted_content = f.read()
    
    with open(sample_encrypted_file['input_file'], 'r') as f:
        original_content = f.read()
    
    assert decrypted_content == original_content

def test_file_not_found(encryption_key):
    with pytest.raises(FileNotFoundError):
        decrypt_file('nonexistent_file.bin', 'output.txt', encryption_key)

def test_invalid_key(sample_encrypted_file):
    invalid_key = Fernet.generate_key()
    with pytest.raises(ValueError):
        decrypt_file(
            sample_encrypted_file['encrypted_file'], 
            sample_encrypted_file['decrypted_file'], 
            invalid_key
        )

def test_invalid_key_type(sample_encrypted_file):
    with pytest.raises(ValueError):
        decrypt_file(
            sample_encrypted_file['encrypted_file'], 
            sample_encrypted_file['decrypted_file'], 
            "not a bytes key"
        )