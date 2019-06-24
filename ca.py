import socket
import time

# CA starting up server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9999)
sock.bind(server_address) ; print('Starting up on {} port: {}'.format(*server_address))
sock.listen(1); print('Waiting for a connection...')

# CA gets registration from server
connection, client_address = sock.accept() ; print('Connected to:', client_address) ; print('Waiting to receive data...')
serverName = connection.recv(100); print('CA has received key from server:', serverName.decode())
publicKey = connection.recv(100); print('CA has received key from server:', publicKey.decode())
decodedPubKey = publicKey.decode()
certificate = connection.recv(100); print('CA has received key from server:', certificate.decode())
print('waiting for more connections...')
#connection.close(); print('Closing connection to server')

# CA receives client request and verifies if authentic
connection, client_address = sock.accept() ; print('Connected to:', client_address) ; print('Waiting to receive data...')
serverName = connection.recv(100); print('CA has received:', serverName.decode()) ; time.sleep(1)
if serverName.decode() == certificate.decode():
    connection.sendall(decodedPubKey.encode('utf-8')); print('sending: ', decodedPubKey) ; time.sleep(1)
else:
    output = 'certificate not valid'
    connection.sendall(decodedPubKey.encode('utf-8')); print(output); time.sleep(1)

connection.close(); print('Closing connection')

