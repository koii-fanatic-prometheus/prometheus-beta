import pytest
from src.file_extension import get_file_extension

def test_get_file_extension_basic():
    """Test basic file extension extraction."""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('image.jpg') == 'jpg'
    assert get_file_extension('script.py') == 'py'

def test_get_file_extension_multiple_dots():
    """Test files with multiple dots."""
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('complex.file.name.txt') == 'txt'

def test_get_file_extension_no_extension():
    """Test files without an extension."""
    assert get_file_extension('README') == ''
    assert get_file_extension('makefile') == ''

def test_get_file_extension_with_path():
    """Test file extensions in file paths."""
    assert get_file_extension('/home/user/document.txt') == 'txt'
    assert get_file_extension('C:\\Users\\name\\file.docx') == 'docx'

def test_get_file_extension_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])