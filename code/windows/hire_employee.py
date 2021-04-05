from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase
from Proyect.database_conect.functions.validate import *


class HireEmployee(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container = dict(self.database.jobs())
        self.var_reload = 0

    # Return jobs from database
    def return_post(self):
        self.container = dict(self.database.jobs())
        job_name_list = []

        for key in self.container:
            job_name_list.append(self.container[key])

        return job_name_list

    def reload(self):
        self.var_reload = 0

    # Returns the id of the address that was added
    @staticmethod
    def insert_address(address):
        return valid_address(address)

    def add_employee(self, users, address):
        if self.var_reload != 0:
            return "Reload the screen"

        print("\nUsuario sin validar: ", users)  # str
        print("print address validada: ", address)
        user = users.split(',')
        print(user[1])

        if address == 1:
            return "The address is incorrect"
        if address == 2:
            return "Ingrese al menos un barrio y una calle"

        # Check that there is a jobs
        for key in self.container:
            if self.container[key] == user[1]:
                user[1] = key
        if user[1] == "deploy":
            return "Elija un cargo"

        result = valid_insert_user(user)
        if type(result) != list:
            print("result", result)
            return result
        else:
            id_address = self.database.insert_address(address)
            result[3] = id_address
            employee_str = str(result)
            employee_str = employee_str.replace("[", "")
            employee_str = employee_str.replace("]", "")
            employee_str = employee_str.replace("'null'", "null")
            print("\nInserting: ", employee_str)
            user_ide = self.database.insert_employee(employee_str)

        self.var_reload = 1
        return f"User created with id: {user_ide}"
