# Listen using `nc -l -p 1337` and run this script to send a message to the listener
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 1337))
s.sendall(b'Hello, world')

data = s.recv(1024)
s.close()

print('Received', repr(data))