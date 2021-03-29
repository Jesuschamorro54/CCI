from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase


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

    def add_employee(self, users, address):
        print(users)
        print(address)
        pass


