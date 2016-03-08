# _*_ coding utf-8 _*_
import socket

infos = socket.getaddrinfo('127.0.0.1', 5000)
stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
client = socket.socket(*stream_info[:3])
client.connect(stream_info[-1])

msg = u'this is the message to send.....'
client.sendall(msg.encode('utf-8'))


buffer_length = 8
message_complete = False

while not message_complete:
    data = client.recv(buffer_length)
    print(data.decode('utf-8'))
    if len(data) < buffer_length:
        break

client.close()
