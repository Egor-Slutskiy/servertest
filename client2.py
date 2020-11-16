import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
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


def msg_scan():
    msg = input('your message: ')
    if msg and msg != "!DISCONNECT":
        send(msg)
    if msg == "!DISCONNECT":
        send(DISCONNECT_MESSAGE)
    msg_scan()


def server_scan():
    print(client.recv(2048).decode(FORMAT))
    server_scan()


server_scan_thread = threading.Thread(target=server_scan)
msg_scan_thread = threading.Thread(target=msg_scan)

server_scan_thread.start()
msg_scan_thread.start()