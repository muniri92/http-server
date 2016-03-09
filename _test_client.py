# _*_ coding utf-8 _*_


def test_client():
	from client import send
	message = "hello"
	assert send(message) == "HTTP/1.1 200 OK"