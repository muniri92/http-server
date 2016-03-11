# _*_ coding utf-8 _*_
"""Simple HTTP server."""
import socket

# address = ('127.0.0.1', 5000)
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
# server.bind(address)
# server.listen(1)
# conn, addr = server.accept()
# buffer_length = 32


def server_fun():
    """Set server to listen and return URI."""
    message_sending = True
    while message_sending:
        part = conn.recv(buffer_length)
        try:
            URI = parse_request(part)
        except NameError:
            method_error = "HTTP/1.1 405 Method Not Allowed\r\n"
            conn.sendall(method_error.decode('utf-8'))
        except TypeError:
            version_error = "HTTP/1.1 Version Not Supported\r\n"
            conn.sendall(version_error.decode('utf-8'))
        except AttributeError:
            missing_error = "HTTP/1.1 400 Bad Request"
            conn.sendall(missing_error.decode('utf-8'))
        if not part:
            break
        message_sending = False


def parse_request(request):
    """Make sure client request is decent."""
    temp_list = request.split("\r\n")
    part_list = temp_list[0].split(' ')
    print part_list
    if len(part_list) < 3:
        raise AttributeError
    elif part_list[0] != 'GET':
        raise NameError
    elif part_list[2] != "HTTP/1.1":
        raise TypeError
    else:
        return part_list[1]

if __name__ == "__main__":
    address = ('127.0.0.1', 5000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()
    buffer_length = 32

    server_fun()
    conn.close()
