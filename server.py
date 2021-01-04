import socket
import select
import threading

"""
Command format:
 - "packet_length, "
"""


class CommandServer:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.SOCK_STREAM, socket.AF_INET)
        self.tcp_transfer_server = None
        self.udp_transfer_server = None
        self.ip = ip
        self.port = port
        self.server_on = True
        self.clients = []
        self.initSocket()
        self.run()

    def initSocket(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen(5)

    def run(self):
        while self.server_on:
            # Check for incoming connection
            r_list, w_list, x_list = select.select([self.socket], [], [], 0.05)
            for client in r_list:
                # Async accept process
                threading.Thread(target=lambda arg=client: self.acceptClient(arg)).start()

    def acceptClient(self, client):
        client_socket, _ = client.accept()
        # Wait for incoming packet with additional connections
        # Message format: "connect|username|password"
        command = client_socket.recv(1024)
        # Add client to global list
        server_client = {
            "client": client_socket,
            "public_key": None
             }
        self.clients.append(server_client)

    def sendMessage(self, client, message):
        pass

    def encryptMessage(self, client, message):
        pass


class TCPTransferServer(threading.Thread):
    def __init__(self):
        super().__init__()


class UDPTransferServer(threading.Thread):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    # command_server = CommandServer("localhost", 20000)
    print(int("10001", 2))
    pass
