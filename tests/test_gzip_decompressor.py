import os
import gzip
import pytest
from src.gzip_decompressor import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmpdir):
    """Create a sample gzip file for testing."""
    input_path = os.path.join(tmpdir, 'sample.txt.gz')
    with gzip.open(input_path, 'wb') as f:
        f.write(b'Hello, World!')
    return input_path

def test_decompress_gzip_file(sample_gzip_file, tmpdir):
    """Test successful gzip file decompression."""
    output_path = os.path.join(tmpdir, 'decompressed.txt')
    result = decompress_gzip_file(sample_gzip_file, output_path)
    
    assert result == output_path
    assert os.path.exists(output_path)
    
    with open(output_path, 'rb') as f:
        assert f.read() == b'Hello, World!'

def test_decompress_gzip_file_default_output(sample_gzip_file, tmpdir):
    """Test decompression with default output path."""
    result = decompress_gzip_file(sample_gzip_file)
    
    assert result.endswith('sample.txt')
    assert os.path.exists(result)
    
    with open(result, 'rb') as f:
        assert f.read() == b'Hello, World!'

def test_nonexistent_file():
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file('non_existent_file.gz')

def test_directory_input(tmpdir):
    """Test handling of directory input."""
    with pytest.raises(IsADirectoryError):
        decompress_gzip_file(str(tmpdir))

def test_invalid_gzip_file(tmpdir):
    """Test handling of invalid gzip file."""
    invalid_file = os.path.join(tmpdir, 'invalid.gz')
    with open(invalid_file, 'wb') as f:
        f.write(b'Not a gzip file')
    
    with pytest.raises(ValueError, match='not a valid gzip file'):
        decompress_gzip_file(invalid_file)