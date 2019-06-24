import socket
import time

# Registering on CA server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ca_address = ('localhost', 9999)
sock.connect(ca_address); print('Connecting to {} port: {}'.format(*ca_address))
serverName = 'PeterServer' ; sock.sendall(serverName.encode('utf-8')); print('Sending:', serverName); time.sleep(1)
publicKey = 'MyPassPhrase' ; sock.sendall(publicKey.encode('utf-8')); print('Sending:', publicKey); time.sleep(1)
certificate = 'MyCertificate' ; sock.sendall(certificate.encode('utf-8')); print('Sending:', certificate); time.sleep(1)
sock.close(); print('Closing socket')

# Server Staring Up
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9500)
sock.bind(server_address) ; print('Starting up on {} port: {}'.format(*server_address))

# Getting initial contact from client and Sending the Client a Certificate
sock.listen(1); print('Waiting for a connection...')
connection, client_address = sock.accept(); print('Connected to:', client_address); print('Waiting to receive data...')
data = connection.recv(100); print('Server has received:', data.decode()); time.sleep(1); print('Sending back certificate')
connection.sendall(certificate.encode('utf-8')) ; print('Sending:', certificate)
connection.close(); print('Closing connection')

# Server verifies public key
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9500)
sock.bind(server_address) ; print('Starting up on {} port: {}'.format(*server_address))
sock.listen(1); print('Waiting for a connection...')
connection, client_address = sock.accept(); print('Connected to:', client_address); print('Waiting to receive data...')
clientPublicKey = connection.recv(100); print('server has received:', clientPublicKey.decode())
if clientPublicKey.decode() == publicKey:
    output = 'authenticated'; connection.sendall(output.encode('utf-8')); print(output)
else:
    output = 'public key not valid'
    connection.sendall(output.encode('utf-8')); print(output)

#Server has conversation with client
rec1 = connection.recv(100); print('server has received:', rec1.decode())
mess1 = 'How are you?'
connection.sendall(mess1.encode('utf-8')); print('sending: ', mess1)
rec2 = connection.recv(100); print('server has received:', rec2.decode())
mess2 = 'Thats great, have a good one!'
connection.sendall(mess2.encode('utf-8')); print('sending: ', mess2)
sock.close(); print('Closing connection')

