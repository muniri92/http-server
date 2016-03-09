# _*_ coding utf-8 _*_
"""Echo server Client test"""


def test_server():
	  """Test function for Client echo server."""
    from client import send
    message = "hello"
    assert send(message) == "hello"
