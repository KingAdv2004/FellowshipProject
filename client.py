import socket
import threading

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# connect to the server on local machine
server = socket.gethostbyname(socket.gethostname())
server_binding = (server, 9999) 
cs.connect(server_binding)

# recieve data from server: Enter your username  
data_from_server=cs.recv(1024)
message = data_from_server.decode()
cs.send(input("Username: ").encode())

# IN GROUPS
# receive data from server: Enter a valid password
data_from_server=cs.recv(1024)
message = data_from_server.decode()
cs.send(input("Password: ").encode())

# close the client sockets
cs.close()
exit()