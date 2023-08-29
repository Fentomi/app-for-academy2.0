from server_config import SERVER_IP, SERVER_PORT
import socket
import pickle
from database_controller import Database


class Server():
    #create server
    def create(self, ip_server: str, port_server: int) -> None:
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((ip_server, port_server))
            print('Server created [ACCESS]')
            print('~' * 30)
        except:
            print('Server created [DENIED]')

    #open server for connections and transactions data
    def open(self) -> None:
        self.server.listen()

        while True:
            #client connected
            conn, addr = self.server.accept()
            print(f'{addr[0]} connected.')

            #load sql-request
            sql_request = pickle.loads(conn.recv(1024))
            print(f'sql_request: {sql_request}')

            #send sql-request in database and get data
            data = self.send_request_in_database(sql_request)
            print(f'data is: {data}')

            #send client data
            conn.send(pickle.dumps(data))

            #close connection with client
            conn.close()
            print(f'connection close')
            print('~' * 30)

    #send sql-request on database and return tuple or bool result
    def send_request_in_database(self, sql_request: str) -> (bool, tuple):
        database = Database()
        database.create_connect()
        return database.send_sql_request(sql_request)


def main():
    server = Server()
    server.create(SERVER_IP, SERVER_PORT)
    server.open()

if __name__ == '__main__':
    main()