import pymysql
from Proyect.database_conect.functions.validate import *
from Proyect.database_conect.functions.insertions import *

class DataBase:
    def __init__(self, name_data_base):
        self.name = name_data_base
        self.connection = pymysql.connect(host='localhost', user='root', password='20023006', db=f'{name_data_base}')
        self.cursor = self.connection.cursor()
        self.container = None
        print("Established Connection")


    # Valid login
    def valid_login(self, ide, post):
        return valid_login_func(self.cursor, ide, post)

    # Returned jobs for login
    def jobs(self):
        sql = "select id, nombre from cargos"
        self.cursor.execute(sql)
        self.container = self.cursor.fetchall()
        return self.container

    def insert_address(self, address):
        insert_address_func(self.cursor, address)
        self.connection.commit()
        self.cursor.execute("SELECT last_insert_id()")
        id = self.cursor.fetchone()
        print("imprimir id: ", id)
        return id[0]


