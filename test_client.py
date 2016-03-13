# _*_ coding utf-8 _*_
"""Test to make sure the correct response is given."""
import pytest


def test_ok():
    """Test to get correct server response."""
    from server import response_ok
    assert response_ok() == b'HTTP/1.1 200 OK\r\n'


def test_error():
    """Test to get an error response."""
    from server import response_error
    assert response_error() == b'HTTP/1.1 500 InternalServerError\r\n'
