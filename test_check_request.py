# _*_ coding utf-8 _*_
"""Test for client request parsing."""
import pytest


def test_method_request():
    """Test to match method."""
    from server import parse_request
    with pytest.raises(NameError):
        parse_request("POST /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")


def test_version_request():
    """Test to match http version."""
    from server import parse_request
    with pytest.raises(TypeError):
        parse_request("GET /hello.html HTTP/1.0\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")


def test_complete_header():
    """Test to make sure header is complete."""
    from server import parse_request
    with pytest.raises(AttributeError):
        parse_request("GET HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")


def test_good_request():
    """Test function returns URI."""
    from server import parse_request
    assert parse_request("GET /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n") == "/hello.html"
