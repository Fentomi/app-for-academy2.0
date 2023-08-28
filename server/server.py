from server_config import SERVER_IP, SERVER_PORT
import socket
import sqlite3


class Server():
    def create_server(self) -> None:
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((SERVER_IP, SERVER_PORT))
            print('Create server [ACCESS]')
        except:
            print('Create server [ERROR]')

    def open_server(self):
        self.server.listen()
        print('Server is listen...')
        while True:
            user, data = self.server.accept()
            print(f'Server find a friend! it\'s {user}')


def main():
    server = Server()
    server.create_server()
    server.open_server()


if __name__ == '__main__':
    main()