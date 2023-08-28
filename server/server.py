from server_config import SERVER_IP, SERVER_PORT
import socket


class Server():
    def __init__(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((SERVER_IP, SERVER_PORT))
            print('Create server [ACCESS]')
        except:
            print('Create server [DENIED]')

    def open_server(self):
        self.server.listen()
        print('Server is listen...')
        while True:
            self.user, self.data = self.server.accept()
            print(f'Server find a friend! it\'s {self.user}')
            self.get_request_from_client()

    def get_request_from_client(self):
        request = self.user.recv(10000).decode('utf-8')
        print(request)


def main():
    server = Server()
    server.open_server()


if __name__ == '__main__':
    main()