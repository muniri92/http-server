# _*_ coding utf-8 _*_
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
client.connect(5000)

msg = u'this is the message to send'
client.sendall(msg.encode('utf-8'))
