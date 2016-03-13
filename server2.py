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
                        # Im not positive this if statement is needed, but everything is
                        # working so it's staying for now
                        pass
                    elif len(data) < buffer_length:
                        # full request has been received
                        try:
                            # check for uri request for errors
                            uri = parse_request(data)
                            # generate response based on file type
                            new_uri = route_uri(server_path, uri)
                            # send response to browser/client
                            conn.sendall(new_uri)
                        except AttributeError:
                            # uri missing data
                            missing_error = "HTTP/1.1 400 Bad Request\r\n"
                            conn.sendall(missing_error.decode('utf-8'))
                        except NameError:
                            # uri has unsupported method
                            method_error = "HTTP/1.1 405 Method Not Allowed\r\n"
                            conn.sendall(method_error.decode('utf-8'))
                        except TypeError:
                            # uri has http version other than 1.1
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


def response_ok(path, uri, file_type):
    """Create customized HTTP response for route_uri()."""
    return_path = os.path.join(path, uri)
    if "image" in file_type:
        open_file = io.open(return_path, 'rb')
    else:
        open_file = io.open(return_path)
    read_file = open_file.read()
    open_file.close()
    html_response = "HTTP/1.1 200 OK\r\nContent-Type: {}\r\n\r\n".format(file_type) + read_file
    return html_response


def generate_html(base_path, uri):
    """Create html code to display files."""
    if uri == "/" or uri == "":
        join_path = base_path
    else:
        join_path = os.path.join(base_path, uri)
    path = os.walk(join_path)
    walk_path = next(path)
    show_dir = walk_path[1]
    show_files = walk_path[2]
    inject_html_dir = ""
    inject_html_file = ""
    if len(show_dir) > 0:
        for directory in show_dir:
            inject_html_dir += "<li><a href={}>{}</a></li>".format(os.path.join(uri, directory), directory)
    else:
        inject_html_dir = "No Directories"
    if len(show_files) > 0:
        for file in show_files:
            inject_html_file += "<li><a href={}>{}</a></li>".format(os.path.join(uri, file), file)
    else:
        inject_html_file = "No Files"
    return_path = "Directories:<ul>{}</ul></br>Files:<ul>{}</ul>".format(inject_html_dir, inject_html_file)
    return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + return_path


def route_uri(base_path, uri):
    """Check to see what file type GET is looking for."""
    # We have to remove the FIRST slash in the requested uri or else it throws off os.path.join()
    uri_no_slash = uri.replace("/", "", 1)
    if "." not in uri:
        return generate_html(base_path, uri_no_slash)
    elif ".html" in uri:
        return response_ok(base_path, uri_no_slash, "text/html")
    elif ".py" in uri:
        return response_ok(base_path, uri_no_slash, "text/py")
    elif ".txt" in uri:
        return response_ok(base_path, uri_no_slash, "text/plain")
    # images
    elif ".jpg" in uri:
        return response_ok(base_path, uri_no_slash, "image/jpeg")
    elif ".png" in uri:
        return response_ok(base_path, uri_no_slash, "image/png")
    else:
        return "/"


if __name__ == "__main__":
    server_func()
