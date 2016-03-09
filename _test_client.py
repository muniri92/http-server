# _*_ coding utf-8 _*_


def test_server():
	from client import send
	message = "hello"
	assert send(message) == "hello"