import socket
from _thread import *
from datetime import datetime

client = socket.socket()
client.connect(('192.168.26.149', 12346))
hostname = socket.gethostname()

def server_thr(client):
    while(True):
        data = client.recv(1024)
        if (socket.gethostbyname(hostname) == '192.168.26.149'):
            print("Diana:", data.decode() + "\t" + datetime.now().strftime("%H:%M %d/%m/%Y"))
        else:
            print("Dana:", data.decode() + "\t" + datetime.now().strftime("%H:%M %d/%m/%Y"))

start_new_thread(server_thr, (client, ))

while(True):
    message = input()
    client.send(message.encode())


