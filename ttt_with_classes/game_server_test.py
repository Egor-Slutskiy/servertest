import socket
import threading
from classes import Connection

HEADER = 64  # сколько байтов может содержать сообщение       было 64 строки, стало 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)  # запихуеваем в лист
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
CONNECTED_LIST = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокет объекта по фаблону
server.bind(ADDR)  # биндим сервер и порт


def handle_client(conn):
    try:
        while conn.connected:
            msg = conn.get_msg()
            if msg:  # если получает от клиента сообщение которое устраивает то
                if msg == DISCONNECT_MESSAGE:
                    conn.disconnect()
                    del CONNECTED_LIST[CONNECTED_LIST.index(conn)]
                if len(CONNECTED_LIST) == 1:
                    CONNECTED_LIST[0].send_msg('play x')
                if len(CONNECTED_LIST) == 2:
                    CONNECTED_LIST[1].send_msg('play o')
                if len(CONNECTED_LIST) == 2:
                    if CONNECTED_LIST.index(conn) == 0:
                        CONNECTED_LIST[1].send(msg)
                    elif CONNECTED_LIST.index(conn) == 1:
                        CONNECTED_LIST[0].send(msg)
                if msg == 'my move is':
                    if CONNECTED_LIST.index(conn) == 0:
                        CONNECTED_LIST[0].send_msg('play x')
                    else:
                        CONNECTED_LIST[1].send_msg('play o')
        conn.disconnect()
    except WindowsError:
        print(f"[ERROR] {conn} client crash")
        del CONNECTED_LIST[CONNECTED_LIST.index(conn)]


# функция запуска сервера на прослушивание
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn = Connection(server.accept())  # если есть коннект клиента то он принимается. conn - объект сокет, addr -
        # адрес и порт клиента
        CONNECTED_LIST.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, ))  # какая-то хуерга которая передает клиента в функцию выше
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


start()