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

    def insert_address(self, address_str):
        print("\ncomo str: ", address_str)
        address = address_str.split(',')
        print("como vector: ", address)

        # check the data that will be sent to the address table
        for i in range(len(address)):
            if address[i] == "":
                address[i] = "null"
            if address[4] != "null":
                try:
                    address[4] = int(address[4])
                except:
                    print("El valor no es tipo numerico")
                    return None
        address_str = str(address)
        address_str = address_str.replace("['", "('")
        address_str = address_str.replace("']", "')")
        self.database.insert_address(address_str)

    def add_employee(self, users, address):
        print(users)
        print("imprimiendo desde add_employee: ", address)






