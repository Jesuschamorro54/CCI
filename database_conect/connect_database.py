import pymysql
from Proyect.database_conect.functions.validate import *
from Proyect.database_conect.functions.insertions import *


class DataBase:
    def __init__(self, name_data_base):
        self.name = name_data_base
        self.connection = pymysql.connect(host='localhost', user='root', password='20023006', db=f'{self.name}')
        self.cursor = self.connection.cursor()
        self.container = None
        self.logger = None
        print(Color.CONNECTION_TEXT)

    # Valid login
    def valid_login(self, ide, post):
        if valid_login_func(self.cursor, ide, post):
            self.logger = ide
            return True

    # Returned all employee
    def employee(self):
        sql = 'select * from empleados'
        self.cursor.execute(sql)
        self.container = self.cursor.fetchall()
        return self.container

    # Returned employee
    def employee_session(self, ide):
        sql = f'select nombre from empleados where id = {ide}'
        self.cursor.execute(sql)
        name = self.cursor.fetchone()
        return name[0]

    # Returned all services
    def services(self):
        self.connection.begin()
        sql = 'select * from servicies'
        self.cursor.execute(sql)
        self.container = self.cursor.fetchall()
        return self.container

    # Returned implement for view
    def implement(self, seeker, identifier):
        self.connection.begin()
        if identifier == 1:
            sql = """
                SELECT imp.id, imp.nombre, imp.belonging, prov.nombre, imp.estado, imp.descriptions 
                FROM implementos imp, proveedores prov
                WHERE prov.id = imp.proveedor"""
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

        self.cursor.execute("SELECT last_insert_id()")
        ide = self.cursor.fetchone()
        return ide[0]

    # Add maintenance
    def insert_maintenance(self, authorized, assigned, date, option):
        insert_maintenance_func(self.cursor, self.connection, authorized, assigned, date, option)
        self.connection.commit()

        # Returned id of maintenance
        self.cursor.execute("SELECT last_insert_id()")
        ide = self.cursor.fetchone()
        return ide[0]

    # Add recent
    def insert_recent(self, maintenance, implement, assigned, option):
        self.connection.begin()
        insert_recent_func(self.cursor, self.connection, maintenance, implement, assigned, option)
        self.connection.commit()

    # Update state of implement
    def update_implement(self, ide, state):
        # Print to check
        print("\nUpdating implement...")
        self.connection.begin()
        sql = f"update implementos set estado = {state} where id = {ide}"
        self.cursor.execute(sql)
        self.connection.commit()

    def maintenance(self, seeker, identifier):
        self.connection.begin()
        # Date
        if identifier == 1:
            sql = f"""
                    SELECT r.id, emp.nombre, main.entity, main.assigned, r.maintenance, imp.nombre, r.date, main.programmed, main.estado  FROM recents r
                    INNER JOIN mantenimiento main on main.id = r.maintenance INNER JOIN empleados emp on emp.id = main.authorized
                    LEFT JOIN servicies serv on serv.id = main.entity INNER JOIN implementos imp on imp.id = r.implement
                    WHERE locate("{seeker}", main.programmed);"""
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            print("Returned data...", self.container)
            return self.container
        # Implement
        elif identifier == 2:
            sql = f"""
                SELECT r.id, emp.nombre, main.entity, main.assigned, r.maintenance, imp.nombre, r.date, main.programmed, main.estado  FROM recents r
                INNER JOIN mantenimiento main on main.id = r.maintenance INNER JOIN empleados emp on emp.id = main.authorized
                LEFT JOIN servicies serv on serv.id = main.entity INNER JOIN implementos imp on imp.id = r.implement
                WHERE locate("{seeker}", imp.nombre);"""
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            return self.container
        # Maintenance
        elif identifier == 3:
            sql = f"""
                SELECT r.id, emp.nombre, main.entity, main.assigned, r.maintenance, imp.nombre, r.date, main.programmed, main.estado  FROM recents r
                INNER JOIN mantenimiento main on main.id = r.maintenance AND main.id in ({seeker}) JOIN empleados emp on emp.id = main.authorized
                LEFT JOIN servicies serv on serv.id = main.entity INNER JOIN implementos imp on imp.id = r.implement;"""
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            return self.container
        elif identifier == 4:
            sql = f"""
                SELECT r.id, emp.nombre, serv.nombre, main.assigned, r.maintenance, imp.nombre, r.date, main.programmed, main.estado FROM recents r
                INNER JOIN mantenimiento main on main.id = r.maintenance JOIN empleados emp on emp.id = main.authorized
                LEFT JOIN servicies serv on serv.id = main.entity INNER JOIN implementos imp on imp.id = r.implement;"""
            self.cursor.execute(sql)
            self.container = self.cursor.fetchall()
            return self.container



class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'
    CONNECTION_TEXT = f"{RED}[{GREEN}INFO   {RED}] {RED}[{MAGENTA}BD          {RED}]{RED} successful database connection{RESET}"
