import socket

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to server
print('initiatiing connection to server')
server_address = ('localhost', 9500)
print('Connecting to {} port: {}'.format(*server_address))
sock.connect(server_address)
#initiating contact
output = 'Lets connect!'
print('Sending:', output)
sock.sendall(output.encode('utf-8'))
#Receiving certificate
data = sock.recv(100)
print('Received from server:', data.decode())




#connecting to CA
print('initiatiing connection to certificate authenticator')
ca_address = ('localhost', 9999)
print('Connecting to {} port: {}'.format(*server_address))
sock.connect(server_address)









# Client makes initial contact to server and receives certificate



# Client contacts CA to find if certificate is valid, gets public key



# Client sends public key to Server




















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








#3 client initiates contact with server
#5 client gets key
#6 clent asks CA if legit
#9 client receives the go ahead
#10 client proceeds to communicate with server