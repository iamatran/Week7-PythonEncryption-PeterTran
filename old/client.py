import socket

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the socket to the port where the server is listening
server_address = ('localhost', 9500)
print('Connecting to {} port: {}'.format(*server_address))
sock.connect(server_address)

# Sending the inputed data
output = input('What do you want to send? ')
print('Sending:', output)
sock.sendall(output.encode('utf-8'))

# Getting a response
data = sock.recv(100)
print('Received from server:', data.decode())

# Closing socket
print('Closing socket')
sock.close()