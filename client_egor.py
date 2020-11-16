import socket
import time

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.14"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# функция отправки на сервер
def send_msg(msg):
    client.send(msg.encode(FORMAT))
    print(client.recv(HEADER).decode(FORMAT))


# функция которая ждет ввод и отправляет на сервер
def input_scan():
    msg = input()
    if msg and msg != "!DISCONNECT":
        send_msg(msg)
    else:
        send_msg('ping')
    if msg == "!DISCONNECT":
        send_msg(DISCONNECT_MESSAGE)
    input_scan()


def server_scan():
    while True:
        msg = 'ping'
        send_msg(msg)
        time.sleep(1)


input_scan()
server_scan()