import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

@pytest.fixture(autouse=True)
def reset_logging():
    """Reset logging between tests to ensure clean test environment"""
    logging.getLogger().handlers.clear()
    logging.getLogger().setLevel(logging.NOTSET)

def test_log_variable_type_primitive_types():
    """Test logging of primitive types"""
    # Capture logging output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

    # Test integer
    result = log_variable_type(42)
    assert result == 'int'
    assert 'Variable type: int' in log_capture.getvalue()

    # Test string
    log_capture.truncate(0)
    log_capture.seek(0)
    result = log_variable_type("hello")
    assert result == 'str'
    assert 'Variable type: str' in log_capture.getvalue()

def test_log_variable_type_complex_types():
    """Test logging of complex types"""
    # Capture logging output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

    # Test list
    result = log_variable_type([1, 2, 3])
    assert result == 'list'
    assert 'Variable type: list' in log_capture.getvalue()

    # Test dictionary
    log_capture.truncate(0)
    log_capture.seek(0)
    result = log_variable_type({'a': 1, 'b': 2})
    assert result == 'dict'
    assert 'Variable type: dict' in log_capture.getvalue()

def test_log_variable_type_edge_cases():
    """Test logging of various edge case types"""
    # Capture logging output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

    # Test None
    result = log_variable_type(None)
    assert result == 'NoneType'
    assert 'Variable type: NoneType' in log_capture.getvalue()

    # Test custom class
    log_capture.truncate(0)
    log_capture.seek(0)
    class TestClass:
        pass

    test_instance = TestClass()
    result = log_variable_type(test_instance)
    assert result == 'TestClass'
    assert 'Variable type: TestClass' in log_capture.getvalue()