# _*_ coding utf-8 _*_
"""Test to make sure the correct response is given."""
import pytest

ERROR_TEST = ["HTTP/1.1", "500", "InternalServerError\r\n"]


def test_ok():
    """Test to get correct server response."""
    from server import response_ok
    assert response_ok() == "HTTP/1.1 200 OK"


def test_error():
    """Test to get an error response."""
    from server import response_error
    assert response_error().split(" ")[0] == ERROR_TEST[0]
    assert response_error().split(" ")[1] == ERROR_TEST[1]
    assert response_error().split(" ")[2] == ERROR_TEST[2]
