import threading # two things happening at once
import sqlite3
import hashlib
import socket # used to establish the connection between client and server

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, connection oriented protocol (TCP)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9999)
ss.bind(server_binding)
ss.listen()


def start_connection(c): # taking client as parameter
    count = 0
    while(count < 2):  #use loop to send 1, 2, 3, 4, 5 to client
        if (count == 0):
            msg = "Enter your username"
            c.send(msg.encode())
            response = c.recv(1024).decode()
            print("Username: " + response)
            count+=1
        else:
            msg = "Enter a valid password"
            c.send(msg.encode())
            response = c.recv(1024).decode()
            print("Password: " + response)
            count+=1     
while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

# Close the server socket
    ss.close()
    exit()  