from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase


class AddImplement(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container_implement = None
        self.container_supplier = None
        self.identifier = 0
        self.proveedor_id = ""

    def validate(self, name_implement, name_supplier, date, total):
        self.identifier = 0
        # Check that the entered parameters are correct
        if name_implement == "" or name_supplier == "":
            return "Hay casillas vacias"
        elif date == "" or len(date) != 10:
            return "La fecha es invalida"
        elif total == "$0":
            return "¡Ups! Hay algo mal en el precio"

        # instantiate the containers
        self.container_implement = self.database.implement(0, 1)
        self.container_supplier = self.database.suppliers()
        long_implement = len(self.container_implement)
        long_supplier = len(self.container_supplier)

        # Check that the implement entered is already in the database
        for key in range(long_implement):
            if self.container_implement[key][1] == name_implement:
                print("id: ", key, "Nombre: ", self.container_implement[key][1])
                break
            if key == (long_implement - 1) and self.container_implement[key][1] != name_implement:
                self.identifier = 1

        # Check that the supplier entered is already in the database
        for key in range(long_supplier):
            if self.container_supplier[key][1] == name_supplier:
                print("id: ", key, "Nombre: ", self.container_supplier[key][1])
                self.proveedor_id = self.container_supplier[key][0]
                print("True id: ", self.proveedor_id)
                break
            if (key == long_supplier - 1) and self.container_supplier[key][1] != name_supplier:
                self.identifier = 2

        if self.identifier == 1:
            print("dentro")
            self.activate(2)
            return "El implemento no se encuentra en la base de datos ¿Desea agregarlo?"
        if self.identifier == 2:
            print("dentro")
            self.activate(2)
            return "El proveedor no se encuentra en la base de datos ¿Desea agregarlo?"

    def add_new(self, implement, supplier):
        if self.identifier == 1:
            print(implement)

        if self.identifier == 2:
            print(supplier)
            # self.database.insert_supplier(supplier)
            return "El nuevo proveedor se añadió con exito"

    def activate(self, i):
        if i == 1:
            self.comprar.disabled = False
        if i == 2:
            self.add.disabled = False

    def deactivate(self):
        print("se ejecuto")
        self.add.disabled = True

    @staticmethod
    def total(costo, cantidad):
        try:
            costo = int(costo)
            cantidad = int(cantidad)
            return costo * cantidad
        except:
            return "0"
