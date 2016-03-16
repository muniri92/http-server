# _*_ coding utf-8 _*_
"""Simple HTTP server."""
import socket
import io
import os


def server_func():
    """Set server to listen and return URI."""
    buffer_length = 8
    try:
        while True:
            conn, addr = server.accept()
            try:
                while True:
                    data = conn.recv(buffer_length)
                    if data:
                        try:
                            uri = parse_request(part)
                            print(uri)
                            file = os.path.join(server_path, uri)
                            print(file)
                            opened = io.open(file, 'rb')
                            output_file = opened.read()
                            opened.close()
                            conn.sendall('HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n' + output_file)
                        except NameError:
                            method_error = "HTTP/1.1 405 Method Not Allowed\r\n"
                            conn.sendall(method_error.decode('utf-8'))
                        except TypeError:
                            version_error = "HTTP/1.1 505 Version Not Supported\r\n"
                            conn.sendall(version_error.decode('utf-8'))
                        except AttributeError:
                            missing_error = "HTTP/1.1 400 Bad Request"
                            conn.sendall(missing_error.decode('utf-8'))
                    else:
                        conn.shutdown(socket.SHUT_RDWR)
                        break
            finally:
                conn.close()
                break
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
    address = ('127.0.0.1', 5000)
    server_path = "/Users/admin-1/http_server/http-server/webroot/"
    os.cwd(server_path)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(address)
    server.listen(1)
    server_func()
