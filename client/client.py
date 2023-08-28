import socket
from server_config import SERVER_IP, SERVER_PORT

class Client():
    def __init__(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((SERVER_IP, SERVER_PORT))
            print('Connect with server [ACCESS]')
        except:
            print('Connect with server [DENIED]')

    def send_message_on_server(self, text: str) -> None:
        self.client.send(text.encode('utf-8'))


def main():
    client = Client()
    client.send_message_on_server('Example')


if __name__ == '__main__':
    main()