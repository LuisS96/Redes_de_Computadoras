# Import Libraries
import socket

# Set IP Address and Port
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BUFFER_SIZE = 1024

# Open communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Create loop to receive messages from client
while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print "received message:", data
