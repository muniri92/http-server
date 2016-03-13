"""Test server."""
import pytest


def test_method_request():
    """Test to match method."""
    from server import parse_request
    with pytest.raises(NameError):
        parse_request("POST /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")


def test_version_request():
    """Test to match http version."""
    from server import parse_request
    with pytest.raises(TypeError):
        parse_request("GET /hello.html HTTP/1.0\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")


def test_complete_header():
    """Test to make sure header is complete."""
    from server import parse_request
    with pytest.raises(AttributeError):
        parse_request("GET HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")


def test_good_request():
    """Test function returns URI."""
    from server import parse_request
    assert parse_request("GET /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n") == "/hello.html"


def test_generate_html():
    """Test the generartion of an html list."""
    server_path = "/Users/admin-1/http_server/http-server/webroot"
    uri = "images"
    result = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nDirectories:<ul>No Directories</ul></br>Files:<ul><li><a href=images/404.jpg>404.jpg</a></li><li><a href=images/JPEG_example.jpg>JPEG_example.jpg</a></li><li><a href=images/sample_1.png>sample_1.png</a></li><li><a href=images/Sample_Scene_Balls.jpg>Sample_Scene_Balls.jpg</a></li><li><a href=images/test.txt>test.txt</a></li></ul>"
    from server import generate_html
    assert generate_html(server_path, uri) == result


def test_route_uri():
    """Test route_uri function."""
    from server import route_uri
    server_path = "/Users/admin-1/http_server/http-server/webroot"
    uri = "images"
    result = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nDirectories:<ul>No Directories</ul></br>Files:<ul><li><a href=images/404.jpg>404.jpg</a></li><li><a href=images/JPEG_example.jpg>JPEG_example.jpg</a></li><li><a href=images/sample_1.png>sample_1.png</a></li><li><a href=images/Sample_Scene_Balls.jpg>Sample_Scene_Balls.jpg</a></li><li><a href=images/test.txt>test.txt</a></li></ul>"
    assert route_uri(server_path, uri) == result
