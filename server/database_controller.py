import sqlite3


class Database():
    def create_connect(self):
        self.database = sqlite3.connect('database.db')
        self.cursor = self.database.cursor()

    def send_sql_request(self, sql_request: str):
        res = self.cursor.execute(sql_request)
        return res.fetchall()

    def close(self):
        self.database.close()

def main():
    db = Database()
    db.create_connect()
    res = db.send_sql_request('SELECT * FROM learntype;')
    print(res)
    db.close()


if __name__ =='__main__':
    main()