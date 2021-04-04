from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase
from kivy.uix.popup import Popup


class OpenPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message_pop.text = ""


class AddImplement(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container_implement = None
        self.container_supplier = None
        self.ventana = OpenPopup()
        self.identifier = 0

    def validate(self, name_implement, name_supplier):
        if name_implement == "" or name_supplier == "":
            return "Hay casillas vacias"
        self.container_implement = self.database.implement(0, 1)
        self.container_supplier = self.database.suppliers()
        long_implement = len(self.container_implement)
        long_supplier = len(self.container_supplier)
        print(self.container_supplier)
        print(name_implement)

        # Check that the implement entered is already in the database
        for key in range(long_implement):
            if self.container_implement[key][1] == name_implement:
                print("id: ", key, "Nombre: ", self.container_implement[key][1])
                break
            if key == (long_implement -1) and self.container_implement[key][1] != name_implement:
                self.identifier = 1

        # Check that the supplier entered is already in the database
        for key in range(long_supplier):
            if self.container_supplier[key][1] == name_supplier:
                print("id: ", key, "Nombre: ", self.container_supplier[key][1])
                break
            if (key == long_supplier-1) and self.container_supplier[key][1] != name_supplier:
                self.identifier = 2

        if self.identifier == 1:
            self.ventana.open()
            self.ventana.message_pop.text = "El implemento no se encontró registrado en la base de datos ¿Desea agregarlo primero?"
            return
        elif self.identifier == 2:
            self.ventana.open()
            self.ventana.message_pop.text = "El Proveedor no se encontró registrado en la base de datos ¿Desea agregarlo primero?"
            return ""
        else:
            return ""

    def activate(self):
        self.comprar.disabled = False

    @staticmethod
    def total(costo, cantidad):
        try:
            costo = int(costo)
            cantidad = int(cantidad)
            return costo * cantidad
        except:
            return "0"

