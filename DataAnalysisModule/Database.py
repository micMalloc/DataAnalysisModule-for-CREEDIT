import pymysql


class Database:
    connection = None

    def __init__(self, database):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='gml7594!tn',
            db=database,
            charset='utf8'
        )
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def read(self):
        pass


