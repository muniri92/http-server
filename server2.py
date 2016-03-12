"""Simple HTTP server."""
import socket
import io
import os

address = ('127.0.0.1', 5000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server.bind(address)
server.listen(1)
buffer_length = 1024
serve_path = "/Users/admin-1/http_server/http-server/webroot"


def server_func():
    try:

        while True:

            conn, addr = server.accept()

            try:
                while True:
                    data = conn.recv(buffer_length)
                    if len(data) == buffer_length:
                        pass
                    elif len(data) < buffer_length:
                        try:
                            uri = parse_request(data)
                            conn.sendall(uri)
                        except AttributeError:
                            missing_error = "HTTP/1.1 400 Bad Request"
                            conn.sendall(missing_error.decode('utf-8'))
                        except NameError:
                            method_error = "HTTP/1.1 405 Method Not Allowed\r\n"
                            conn.sendall(method_error.decode('utf-8'))
                        except TypeError:
                            version_error = "HTTP/1.1 505 Version Not Supported\r\n"
                            conn.sendall(version_error.decode('utf-8'))
                        conn.close()

            except:
                conn.close()
    except KeyboardInterrupt:

        server.close()


def parse_request(request):
    """Make sure client request is decent."""
    temp_list = request.split("\r\n")
    part_list = temp_list[0].split(' ')
    if len(part_list) < 3:
        raise AttributeError
    elif part_list[0] != 'GET':
        raise NameError
    elif part_list[2] != "HTTP/1.1":
        raise TypeError
    else:
        return part_list[1]

if __name__ == "__main__":
    server_func()
