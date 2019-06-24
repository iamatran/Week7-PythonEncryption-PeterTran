import socket
import time

# Client contacts server
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM); print('initiatiing connection to server')
server_address = ('localhost', 9500)
sock1.connect(server_address); print('Connecting to {} port: {}'.format(*server_address))
output = 'Lets connect'
sock1.sendall(output.encode('utf-8')); print('Sending:', output)

#Receiving certificate from server
certificate = sock1.recv(100)
decodedCert = certificate.decode()
print('Received certificate from server:', certificate.decode()) ; time.sleep(1)
sock1.close(); print('Closing server socket')

# verifying with CA
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); print('initiatiing connection to CA')
ca_address = ('localhost', 9999)
print('Connecting to {} port: {}'.format(*ca_address))
sock.connect(ca_address); print('initiatiing connection to certificate authenticator')
sock.sendall(decodedCert.encode('utf-8')); print('Sending:', decodedCert)

# Client contacts CA to find if certificate is valid, gets public key
publicKey = sock.recv(100);  print('Received public key from ca:', publicKey.decode()) ; time.sleep(2)
decodedPubKey = publicKey.decode()
sock.close(); print('Closing ca socket')

# Client sends public key to Server
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM); print('initiatiing connection to server')
server_address = ('localhost', 9500)
sock1.connect(server_address); print('Connecting to {} port: {}'.format(*server_address))
sock1.sendall(decodedPubKey.encode('utf-8')); print('Sending:', decodedPubKey)
serverResponse = sock1.recv(100); print('client has received:', serverResponse.decode()); 

#Client has conversation with server
mess1 = 'Hi'
sock1.sendall(mess1.encode('utf-8')); print('Sending:', mess1); time.sleep(1)
res1 = sock1.recv(100); print('client has received:', res1.decode()); 
mess2 = 'I am good'
sock1.sendall(mess2.encode('utf-8')); print('Sending:', mess2); time.sleep(1)
res2 = sock1.recv(100); print('client has received:', res2.decode()); 
sock1.close(); print('Closing connection')

