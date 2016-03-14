# _*_ coding utf-8 _*_
"""Test for client request parsing."""
import pytest

PARSE_TEST = [(NameError, "POST /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n"),
              (TypeError, "GET /hello.html HTTP/1.0\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n"),
              (AttributeError, "GET HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")
              ]

# *****************************


@pytest.mark.parametrize("error, result", PARSE_TEST)
def test_response(error, result):
    """Test to make sure correct error is raised."""
    from server import parse_request
    with pytest.raises(error):
        parse_request(result)


def test_good_request():
    """Test function returns URI."""
    from server import parse_request
    assert parse_request("GET /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n") == "/hello.html"
