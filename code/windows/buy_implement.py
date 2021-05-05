from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase


class AddImplement(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.reload = 0
        self.database = DataBase("cci")
        self.container_implement = None
        self.container_supplier = None
        self.identifier = 0
        self.proveedor_id = 0
        self.implement_id = 0

    def validate(self, name_implement, name_supplier, total):
        self.identifier = 0
        # Check that the entered parameters are correct
        if name_implement == "" or name_supplier == "":
            return "Hay casillas vacias"
        elif total == "$0":
            return "¡Ups! Hay algo mal en el precio"

        # instantiate the containers
        self.container_implement = self.database.implement(0, 1)
        self.container_supplier = self.database.suppliers()
        long_implement = len(self.container_implement)
        long_supplier = len(self.container_supplier)

        # Check that the implement entered is already in the database
        for key in range(long_implement):
            if self.container_implement[key][1].lower() == name_implement.lower():
                print("id: ", key, "Nombre: ", self.container_implement[key][1])
                self.implement_id = self.container_implement[key][0]
                print("True id implement:", self.implement_id)
                break
            if key == (long_implement - 1) and self.container_implement[key][1].lower() != name_implement.lower():
                self.identifier = 1

        # Check that the supplier entered is already in the database
        for key in range(long_supplier):
            if self.container_supplier[key][1].lower() == name_supplier.lower():
                print("id: ", key, "Nombre: ", self.container_supplier[key][1])
                self.proveedor_id = self.container_supplier[key][0]
                print("True id supplier: ", self.proveedor_id)
                break
            if (key == long_supplier - 1) and self.container_supplier[key][1].lower() != name_supplier.lower():
                self.identifier = 2

        if self.identifier == 2:
            print("dentro")
            self.activate(2)
            return "Proveedor especificado no encontrado ¿Desea agregarlo?"
        if self.identifier == 1:
            print("dentro")
            self.activate(2)
            return "El implemento no se encuentra en la base de datos ¿Desea agregarlo?"
        else:
            self.activate(1)
            return "¡Verificado!"

        # Create a record of the purchase made

    def add_commodity(self, commodity):
        if self.reload == 1:
            return "Por favor recargue la ventana"
        commodity = commodity.replace('$', '')
        print(commodity)
        self.database.insert_commodity(self.implement_id, self.proveedor_id, commodity)
        self.reload = 1
        return "Se registró la compra con exito"

    def add_new(self, implement, supplier):
        if self.identifier == 1:
            print("implemento enviado: ", implement)
            self.database.insert_implement(implement, self.proveedor_id)
            print(implement)
            return "Implemento agregado"

        if self.identifier == 2:
            print(supplier)
            self.database.insert_supplier(supplier)
            return "El nuevo proveedor se añadió con exito"

    def activate(self, i):
        if i == 1:
            self.comprar.disabled = False
        if i == 2:
            self.add.disabled = False

    def deactivate(self):
        print("se ejecuto")
        self.add.disabled = True

    def reloading(self):
        self.comprar.disabled = True
        self.reload = 0

    @staticmethod
    def total(costo, cantidad):
        try:
            costo = int(costo)
            cantidad = int(cantidad)
            return costo * cantidad
        except:
            return "0"
