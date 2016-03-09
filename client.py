# _*_ coding utf-8 _*_
"""Echo Server file."""
import socket


address = ('127.0.0.1', 5000)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
client.connect(address)


def get_msg():
    """Ask user for message to send."""
    msg = raw_input("what would you like to send? \n >>>>>> ")
    return msg


def send(msg):
    """Function to send user message and recv echo from server."""
    client.sendall(msg.encode('utf-8'))
    data = client.recv(32)
    client.close()
    print (data.decode('utf-8'))
    return (data.decode('utf-8'))


if __name__ == "__main__":
    send(get_msg())
