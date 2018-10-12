import socket

TCP_IP = '10.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
	data = "I'm a Teapot"
	s.send(data)
	data_recv = s.recv(BUFFER_SIZE)
	print data_recv
s.close()
