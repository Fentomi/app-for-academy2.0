import socket
import pickle
from server_config import SERVER_IP, SERVER_PORT

class Client():
    #connect with server
    def connect(self, ip_server: str, port_server: int):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip_server, port_server))

    #send and recv sql-request on server
    def send_and_recv_request_on_server(self, sql_request: str) -> (tuple, bool):
        #send request on server
        self.client.send(pickle.dumps(sql_request))
        #get result with server
        self.data = pickle.loads(self.client.recv(1024))
        if self.data is not None:
            return self.data
        return False

    #close connection with server
    def close(self):
        self.client.close()


def main():
    client = Client()
    client.connect(SERVER_IP, SERVER_PORT)
    answer = client.send_and_recv_request_on_server('Privet!')
    print(answer)
    client.close()


if __name__ == '__main__':
    main()