import socket

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to the port
server_address = ('localhost', 9500)
print('Starting up on {} port: {}'.format(*server_address))
sock.bind(server_address)

# Registering on CA server


# Getting initial contact from client
sock.listen(1)
print('Waiting for a connection...')
connection, client_address = sock.accept()
print('Connected to:', client_address)
print('Waiting to receive data...')
data = connection.recv(100)
print('Server has received:', data.decode())
print('Sending back certificate')

# Sending the Client a Certificate


# 













#Receiving Data
data = connection.recv(100)
print('Server has received:', data.decode())

if data.decode() == 'Hello':
    print('Sending: Hi')
    output = 'Hi'
    connection.sendall(output.encode('utf-8'))

else:
    print('Sending: Goodbye')
    output = 'Goodbye'
    connection.sendall(output.encode('utf-8'))

# Closing the connection
print('Closing connection')
connection.close()



























#1 server registers with CA the public key
#2 server sends back client key
#11 server has conversation with client