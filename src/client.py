# _*_ coding utf-8 _*_

import socket


# address = ('127.0.0.1', 5000)
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
# client.connect(address)

# request = "GET /index.html HTTP/1.1 \r\n"


def send():
    client.sendall(request.encode('utf-8'))
    data = client.recv(32)
    client.close()
    print (data.decode('utf-8'))
    return (data.decode('utf-8'))


if __name__ == "__main__":
    address = ('127.0.0.1', 5000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    client.connect(address)
    request = 'GET images/JPEG_example.jpg HTTP/1.1\r\nUser-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\nHost: www.tutorialspoint.com\r\n\r\n'
    send()
