import socket
import threading

class TicTacToeClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.board = [' '] * 9

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        threading.Thread(target=self.receive_updates).start()

    def receive_updates(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break
                # Process data received from server
            except Exception as e:
                print(e)
                break

    def send_move(self, move):
        self.client_socket.sendall(move.encode())

    def close_connection(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = TicTacToeClient('localhost', 5555)
    client.connect()
