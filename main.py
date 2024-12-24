import socket
from datetime import datetime
from _thread import *

def client_thread (con):
   data = con.recv(1024)
   message = data.decode(1024)
   print (f"клиент прислал{message}")
   message = (message[::-1])

   con.send(message.encode())
   con.close()

server = socket.socket()
host = socket.gethostname()
port = 12345
server.bind((host,port))
server.listen(6)

print ("Сервер запущенн")
while True:
 client,_ = server.accept()
 start_new_thread(client_thread,(client,))