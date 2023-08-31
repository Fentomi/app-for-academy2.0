import sqlite3


class Database():
    def create_connect(self):
        self.database = sqlite3.connect('database.db')
        self.cursor = self.database.cursor()

    def send_sql_request(self, sql_request: str):
        res = self.cursor.execute(sql_request)
        self.database.commit()
        return res.fetchall()

    def close(self):
        self.database.close()

def main():
    db = Database()
    db.create_connect()
    data = '1234'
    learntype = 'МКА'
    learntime = 60
    learnprice_month = 5000
    learnprice_sem = 10000
    learnprice_year = 20000
    res = db.send_sql_request(f'insert into learntype values ({len(data)},\'{learntype}\',{learntime},{learnprice_month},{learnprice_sem},{learnprice_year});')

    db.close()


if __name__ =='__main__':
    main()