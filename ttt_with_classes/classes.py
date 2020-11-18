import socket

# классы: connection, field


class Connection():

    def __init__(self, conn):
        self.address = conn[1][0]
        self.port = conn[1][1]
        self.connection = conn[0]
        self.connected = True
        self.format = 'utf-8'
        self.header = 64
        print(f"[NEW CONNECTION] {f'{self.address}:{self.port}'} connected.")

    def disconnect(self):
        self.connection.close()

    def get_msg(self):
        msg = self.connection.recv(self.header).decode(self.format)
        print(f"[f'{self.address}:{self.port}'] {msg}")
        return msg

    def send_msg(self, msg):
        self.connection.send(msg.encode(self.format))

    def __repr__(self):
        return f'<{self.address}:{self.port}>'

    def __str__(self):
        return f'{self.address}:{self.port}'

