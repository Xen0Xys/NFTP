import socket
import select
import threading


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

    @staticmethod
    def acceptClient(client):
        client_socket, _ = client.accept()
        # Wait for incoming packet with additional connections
        # Message format: "connect|username|password"
        command = client_socket.recv(1024)


class TCPTransferServer(threading.Thread):
    def __init__(self):
        super().__init__()


class UDPTransferServer(threading.Thread):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    command_server = CommandServer("localhost", 20000)
