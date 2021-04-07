import pymysql
from Proyect.database_conect.functions.validate import *
from Proyect.database_conect.functions.insertions import *


class DataBase:
    def __init__(self, name_data_base):
        self.name = name_data_base
        self.connection = pymysql.connect(host='localhost', user='root', password='20023006', db=f'{self.name}')
        self.cursor = self.connection.cursor()
        self.container = None
        print("Established Connection")

    # Valid login
    def valid_login(self, ide, post):
        return valid_login_func(self.cursor, ide, post)

    # Returned implement for view
    def implement(self, seeker, identifier):
        self.connection.begin()
        if identifier == 1:
            sql = "select * from implementos"
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            return self.container
        elif identifier == 2:
            sql = f"select * from implementos where id = {seeker}"
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            return self.container
        elif identifier == 3:
            sql = f"select * from implementos where estado = {seeker}"
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            return self.container
        elif identifier == 4:
            sql = f"select * from implementos where belonging = {seeker}"
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            return self.container

    # Returned areas from company
    def area(self):
        self.connection.begin()
        sql = "select id, nombre from area"
        self.cursor.execute(sql)
        self.container = self.cursor.fetchall()
        return self.container

    # Returned jobs for login
    def jobs(self):
        self.connection.begin()
        sql = "select id, nombre from cargos"
        self.cursor.execute(sql)
        self.container = self.cursor.fetchall()
        return self.container

    # Returned suppliers
    def suppliers(self):
        self.connection.begin()
        sql = "Select * from proveedores"
        self.cursor.execute(sql)
        self.container = self.cursor.fetchall()
        return self.container

    # Add address
    def insert_address(self, address):
        self.connection.begin()
        insert_address_func(self.cursor, address, self.connection)
        self.connection.commit()

        self.cursor.execute("SELECT last_insert_id()")
        ide = self.cursor.fetchone()
        print("print id: ", ide)
        return ide[0]

    # Add employee
    def insert_employee(self, employee):
        self.connection.begin()
        insert_employee_func(self.cursor, employee, self.connection)
        self.connection.commit()

        self.cursor.execute("SELECT last_insert_id()")
        ide = self.cursor.fetchone()
        return ide[0]

    # Add implement
    def insert_implement(self, implement, supplier):
        self.connection.begin()
        insert_implement_func(self.cursor, implement, supplier, self.connection)
        self.connection.commit()

    # Add supplier
    def insert_supplier(self, supplier):
        self.connection.begin()
        insert_supplier_func(self.cursor, supplier, self.connection)
        self.connection.commit()

    # Add commodity
    def insert_commodity(self, implement_id, supplier_id, commodity):
        self.connection.begin()
        insert_commodity_func(self.cursor, implement_id, supplier_id, commodity, self.connection)
        self.connection.commit()

