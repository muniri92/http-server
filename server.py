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
    response_ok = b'HTTP/1.1 200 OK'
    conn.sendall(response_ok)
    return response_ok


def response_error():
    """Return a "500" Error message to client."""
    response_errors = u"HTTP/1.1 500 InternalServerError\r\n"
    conn.sendall(response_errors.encode('utf-8'))
    return response_errors


while message_complete:
    message = conn.recv(buffer_length)
    print(message.decode('utf-8'))
    if not message:
        response_error()
        break
    else:
        response_ok()

conn.close()
