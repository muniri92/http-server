# _*_ coding utf-8 _*_
import socket

address = ('127.0.0.1', 5000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server.bind(address)
server.listen(1)
conn, addr = server.accept()

buffer_length = 16
message_complete = True

def response_ok():
	response_ok = "HTTP/1.1 200 OK"
	conn.sendall(response_ok.decode('utf-8'))

def response_error():
	response_error = "HTTP/1.1 500 Internal Server Error"
	conn.sendall(response_error.decode('utf-8'))

while message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf-8'))
    if not part:
        break
    response_ok()

conn.close()
