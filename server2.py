"""Simple HTTP server."""
import socket
import io
import os

address = ('127.0.0.1', 5000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server.bind(address)
server.listen(1)
buffer_length = 1024
server_path = "/Users/admin-1/http_server/http-server/webroot"


def server_func():
    """Run the server."""
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

                            # here is where we call the beast down below
                            new_uri = route_uri(server_path, uri)

                            # I do not think this str() is good but it is what I came up with for right now
                            conn.sendall(str(new_uri))
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
    print(request)
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


def route_uri(base_path, uri):
    """Check to see what file type GET is looking for."""
    # We have to remove the FIRST slash in the requested uri or else it throws off os.path.join()
    uri_no_slash = uri.replace("/", "", 1)

    # These two ifs show the files and dirs depending on where you are
    if uri == "/":
        path = os.walk(server_path)
        walk_path = next(path)
        show_dir = walk_path[1]
        show_files = walk_path[2]
        return_path = "Directories: {}\nFiles: {}".format(show_dir, show_files)
        return return_path
    elif uri == "/images":
        img_path = os.path.join(base_path, uri_no_slash)
        path = os.walk(img_path)
        walk_path = next(path)
        show_dir = walk_path[1]
        show_files = walk_path[2]
        return_path = "Directories: {}\nFiles: {}".format(show_dir, show_files)
        return return_path

    # Starting here is how we handle the different file extensions
    elif ".html" in uri:
        return_html = os.path.join(base_path, uri_no_slash)
        open_file = io.open(return_html)
        read_file = open_file.read()
        open_file.close()
        html_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + read_file
        return html_response
    elif ".py" in uri:
        return_py = os.path.join(base_path, uri_no_slash)
        open_file = io.open(return_py)
        read_file = open_file.read()
        open_file.close()
        html_response = "HTTP/1.1 200 OK\r\nContent-Type: text/py\r\n\r\n" + read_file
        return html_response
    elif ".txt" in uri:
        return_txt = os.path.join(base_path, uri_no_slash)
        open_file = io.open(return_txt)
        read_file = open_file.read()
        open_file.close()
        html_response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n" + read_file
        return html_response

    # here is where I got stuck, we still need a .png elif too
    elif ".jpg" in uri:
        return_jpg = os.path.join(base_path, uri_no_slash)
        print(return_jpg)
        open_file = io.open(return_jpg, 'r')
        read_file = open_file.read()
        open_file.close()
        html_response = "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n" + read_file
    else:
        return "/"

if __name__ == "__main__":
    server_func()
