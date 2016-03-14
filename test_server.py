"""Test server."""
import pytest

PARSE_TEST = [(NameError, "POST /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n"),
              (TypeError, "GET /hello.html HTTP/1.0\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n"),
              (AttributeError, "GET HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n")
              ]

SERVERandURI = [("/Users/admin-1/http_server/http-server/webroot", "images", "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nDirectories:<ul>No Directories</ul></br>Files:<ul><li><a href=images/404.jpg>404.jpg</a></li><li><a href=images/JPEG_example.jpg>JPEG_example.jpg</a></li><li><a href=images/sample_1.png>sample_1.png</a></li><li><a href=images/Sample_Scene_Balls.jpg>Sample_Scene_Balls.jpg</a></li><li><a href=images/test.txt>test.txt</a></li></ul>")]

# *****************************


@pytest.mark.parametrize("error, result", PARSE_TEST)
def test_response(error, result):
    """Test to make sure correct error is raised."""
    from server import parse_request
    with pytest.raises(error):
        parse_request(result)


def test_good_request():
    """Test function returns URI."""
    from server import parse_request
    assert parse_request("GET /hello.html HTTP/1.1\r\nUser-Agent: Mozilla/4.0 compatible; MSIE5.01; Windows NT\r\nHost: www.tutorialspoint.com\r\n\r\n") == "/hello.html"


@pytest.mark.parametrize("server_path, uri, result", SERVERandURI)
def test_generate_html(server_path, uri, result):
    """Test the generartion of an html list."""
    from server import generate_html
    assert generate_html(server_path, uri) == result


@pytest.mark.parametrize("server_path, uri, result", SERVERandURI)
def test_route_uri(server_path, uri, result):
    """Test route_uri function."""
    from server import route_uri
    assert route_uri(server_path, uri) == result
