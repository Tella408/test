import socket
from _thread import *

def client_thr(conn):
    while(True):
        data = conn.recv(1024)
        message = data.decode()
        print(f"From Client: {message}")
        for client in cl:
            if cl != conn:
             client.send((f"{message}").encode())

server = socket.socket()
server.bind(('192.168.26.149', 12346))
server.listen(5)

print("Server is running")

cl = list()
while True:
    client1, _ = server.accept()
    start_new_thread(client_thr, (client1, ))
    cl.append(client1)