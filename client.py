import socket

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
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# функция которая ждет ввод и отправляет на сервер
def msg_scan():
    msg = input()
    if msg and msg != "!DISCONNECT":
        send(msg)
    if msg == "!DISCONNECT":
        send(DISCONNECT_MESSAGE)
    msg_scan()


msg_scan()