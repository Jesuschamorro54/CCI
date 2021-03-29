import pymysql
from Proyect.database_conect.functions.validate import *


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
