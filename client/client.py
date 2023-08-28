import socket
from server.server_config import SERVER_IP, SERVER_PORT

class Client():
    def __init__(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((SERVER_IP, SERVER_PORT))
            print('Connect with server [ACCESS]')
        except:
            print('Connect with server [DENIED]')


def main():
    client = Client()


if __name__ == '__main__':
    main()