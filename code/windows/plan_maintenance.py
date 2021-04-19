from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase


# noinspection PyCompatibility
class PlanMaintenance(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container_implement = None
        self.container_implement_add = {}
        self.identifier = 0
        self.iterator = 0
        self.implement_id = 0

    def add(self, value):
        self.identifier = 0
        self.container_implement = self.database.implement(0, 1)
        long_implement = len(self.container_implement)
        if value == "":
            return "Escriba algo"

        #  Check that the implement entered is already in the database
        for key in range(long_implement):
            if self.container_implement[key][1].lower() == value.lower():
                print("id: ", key, "Nombre: ", self.container_implement[key][1])
                self.implement_id = self.container_implement[key][0]
                self.container_implement_add[self.implement_id] = self.container_implement[key][1]
                break
            if key == (long_implement - 1) and self.container_implement[key][1] != value:
                return "El implemento no se encuentra en la base de datos"

        print("add...")
        self.rv.data.insert(self.iterator, {'iter.text': str(self.iterator+1), 'name.text': value, 'ide.text': str(self.implement_id)})
        self.iterator += 1
        self.clear()
        return ""

    def update(self, ide, name_text):
        if ide == "" or name_text == "":
            return "Debe llenar todos los campos"
        try:
            ide = int(ide) - 1
        except:
            self.clear()
            return "Numero ingresado es invalido"

        long_implement = len(self.container_implement)
        #  Check that the implement entered is already in the database
        for key in range(long_implement):
            if self.container_implement[key][1].lower() == name_text.lower():
                print("id: ", key, "Nombre: ", self.container_implement[key][1])
                self.implement_id = self.container_implement[key][0]
                self.container_implement_add[self.implement_id] = self.container_implement[key][1]
                break
            if key == (long_implement - 1) and self.container_implement[key][1] != name_text:
                return "El implemento no se encuentra en la base de datos"

        if self.rv.data:
            #  Try to update the data in the corresponding ide
            try:
                self.rv.data[ide]['name.text'] = name_text
                self.rv.data[ide]['ide.text'] = str(self.implement_id)

                self.rv.refresh_from_data()
            except:
                self.clear()
                return "El implemento con este id no se ha agregado"
        else:
            self.clear()
            return "Debe añadir implementos a la lista"
        return ""

    def delete(self):
        if self.rv.data:
            implement = self.rv.data[self.iterator-1]['name.text']
            self.rv.data.pop(self.iterator - 1)
            self.iterator -= 1
            return f"{implement} fue eliminado"
        else:
            return ""

    def confirm(self):
        pass

    def clear(self):
        self.message.text = self.nombre_add.text = ""
        self.id_up.text = self.name_up.text = ""
