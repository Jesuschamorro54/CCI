from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase
from Proyect.database_conect.functions.validate import *


class HireEmployee(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container = dict(self.database.jobs())

    # Return jobs from database
    def return_post(self):
        self.container = dict(self.database.jobs())
        job_name_list = []

        for key in self.container:
            job_name_list.append(self.container[key])

        return job_name_list

    @staticmethod
    def insert_address(address):
        return valid_address(address)

    def add_employee(self, users, address):
        print("\nUsuario sin validar: ", users)  # str
        print("print address validada: ", address)
        user = users.split(',')
        print(user[1])

        if address == 1:
            return "La direción es incorrecta"
        if address == 2:
            return "Ingrese al menos un barrio y una calle"

        # Check that there is a jobs
        for key in self.container:
            if self.container[key] == user[1]:
                user[1] = key
        if user[1] == "deploy":
            return "Elija un cargo"

        result = valid_insert_user(user, address)
        if type(result) != list:
            print("resutado", result)
            return result
        else:
            print("ingresando")

        # Ingresar direccion despues de haber validado el usuario
        self.database.insert_address(address)
        return "OK"
