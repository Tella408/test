import socket

clin = socket.socket()
hostname = socket.gethostname()
port = 12345
clin.connect((hostname,port))
message = str(input("Напишите сообщение: "))
clin.send(message.encode())
data = clin.recv(1024)
print("Сервер прислал: ",data.decode())
clin.close