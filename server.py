# _*_ coding utf-8 _*_
"""Echo Server file."""
import socket

address = (u'127.0.0.1', 5000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server.bind(address)
server.listen(1)
conn, addr = server.accept()
buffer_length = 8
message_complete = True


def response_ok():
    """Return a "200" OK response to client."""
    return (b'HTTP/1.1 200 OK\r\n')


def response_error():
    """Return a "500" Error message to client."""
    return (b'HTTP/1.1 500 InternalServerError\r\n')


while message_complete:
    message = conn.recv(buffer_length)
    print(message.decode('utf-8'))
    if not message:
        conn.sendall(response_error())
        break
    else:
        conn.sendall(response_ok())

conn.close()
