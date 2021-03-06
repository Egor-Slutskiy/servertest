import socket
import threading

HEADER = 64  # сколько байтов может содержать сообщение
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)  # запихуеваем в лист
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# CONNECTED_LIST = []
# CONN_LIST = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокет объекта по фаблону
server.bind(ADDR)  # биндим сервер и порт


def handle_client(conn, addr):
    try:
        print(f"[NEW CONNECTION] {addr} connected.")
        # endpoint_id = CONNECTED_LIST.index(addr) - 1
        # endpoint_addr = CONNECTED_LIST[endpoint_id]
        # endpoint_conn = CONN_LIST[endpoint_id]
        connected = True
        while connected:
            # тут копипаста и много лишнего но пусть будет
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:  # если получает от клиента сообщение которое устраивает то
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)  # декодит сообщение в стринг
                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}] {msg}")
                if msg == "pidr":
                    conn.send("sam pidr".encode(FORMAT))  # енкодит отправляет с сервера на клиент
                # elif msg == "check":
                #    endpoint_conn.sendto("proverka".encode(FORMAT), endpoint_addr)
                else:
                    conn.send("Msg received".encode(FORMAT))

        conn.close()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    except WindowsError:
        print(f"[ERROR] {addr} client crash")


# функция запуска сервера на прослушивание
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()  # если есть коннект клиента то он принимается. conn - объект сокет, addr -
        # адрес и порт клиента

        # CONNECTED_LIST.append(addr)
        # CONN_LIST.append(conn)
        # print(CONN_LIST)
        thread = threading.Thread(target=handle_client,
                                  args=(conn, addr))  # какая-то хуерга которая передает клиента в функцию выше
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


start()
