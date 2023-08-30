import socket
import pickle
from server_config import SERVER_IP, SERVER_PORT

class Client():
    #connect with server
    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((SERVER_IP, SERVER_PORT))

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
    client.connect()
    answer = client.send_and_recv_request_on_server('select * from learntype')
    print(answer)
    client.close()


if __name__ == '__main__':
    main()