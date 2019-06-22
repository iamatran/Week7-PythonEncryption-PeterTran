import socket

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to the port
server_address = ('localhost', 9999)
print('Starting up on {} port: {}'.format(*server_address))
sock.bind(server_address)

# Listening for incoming connections
sock.listen(1)

# Waiting for a connection
print('Waiting for a connection...')
connection, client_address = sock.accept()
print('Connected to:', client_address)
print('Waiting to receive data...')


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








# CA initializes


# Receives public key registration from server 



































#2 CA gets registration
#7 CA receives client request and verifies authentic
#8 CA sends back the ok to client