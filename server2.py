"""Simple HTTP server."""
import socket
import io
import os

address = ('127.0.0.1', 5000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server.bind(address)
server.listen(1)
buffer_length = 8
serve_path = "/Users/admin-1/http_server/http-server/webroot"


def server_func():
    try:

        while True:

            conn, addr = server.accept()

            try:
                while True:
                    data = conn.recv(buffer_length)
                    if len(data) == buffer_length:
                        print(data)
                        print(len(data))
                        print("**********************")
                        conn.sendall(data)
                    elif len(data) < buffer_length:
                        conn.close()
                        break
            except:
                conn.close()
    except KeyboardInterrupt:

        server.close()



# def parse_request(request):
#     """Make sure client request is decent."""
#     temp_list = request.split("\r\n")
#     part_list = temp_list[0].split(' ')
#     if len(part_list) < 3:
#         raise AttributeError
#     elif part_list[0] != 'GET':
#         raise NameError
#     elif part_list[2] != "HTTP/1.1":
#         raise TypeError
#     else:
#         return part_list[1]

if __name__ == "__main__":
    server_func()
