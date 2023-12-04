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

server = socket.gethostbyname(socket.gethostname())
server_binding = (server, 9999) 
ss.bind(server_binding)
ss.listen()


def start_connection(c): 
    # taking client as parameter
    msg = "Enter your username: "
    c.send(msg.encode())
    username = c.recv(1024).decode()
    print("Username: " + username)
    msg = "Enter a valid password: "
    c.send(msg.encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()
    print("Password: " + password)
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM mydatabase WHERE username = ? AND password = ?", (username, password)
    cursor.execute(sql)
    if cursor.fetchall():
        c.send("Login successful!".encode())
    else:
        c.send("Incorrect login credentials".encode())
            
while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

# Close the server sockets
ss.close()
exit()  