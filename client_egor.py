import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.14"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# пока коммитил понял что говно и надо переделать
def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# функция которая ждет ввод и отправляет на сервер
def msg_scan():
    while True:
        msg = input()
        server_msg = client.recv(2048).decode(FORMAT)
        if msg and msg != "!DISCONNECT":
            send(msg)
        elif msg == "!DISCONNECT":
            send(DISCONNECT_MESSAGE)
        elif server_msg:
            print(server_msg)


def server_scan():
    while True:
        msg = client.recv(2048).decode(FORMAT)
        if msg:
            print(msg)


def start():
        thread = threading.Thread(target=msg_scan)
        thread.start()


start()
#server_scan()