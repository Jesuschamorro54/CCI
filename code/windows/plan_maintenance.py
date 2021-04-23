from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase
from Proyect.database_conect.functions.validate import *


# noinspection PyCompatibility
class PlanMaintenance(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container_implement = None
        self.container_services = None
        self.container_employee = None
        self.container_implement_add = {}
        self.identifier = 0
        self.iterator = 0
        self.implement_id = 0

    # -- Press to add -- #
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
        self.rv.data.insert(self.iterator, {'iter.text': str(self.iterator + 1), 'name.text': value,
                                            'ide.text': str(self.implement_id)})
        self.iterator += 1
        self.clear()
        return ""

    # -- Press to update -- #
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

    # -- Press to confirm -- #
    def confirm(self, asig, date, entity):
        global id_employee, id_service

        # check date
        if not valid_date(date):
            return "Fecha invalida"

        # check fields
        if asig == "" or entity == "" or self.rv.data == []:
            return "Debe llenar todos los campos"

        if asig == "Entidad":
            self.container_services = self.database.services()
            long_services = len(self.container_services)
            print(self.container_services)

            #  Check that the service entered is already in the database
            for key in range(long_services):
                if self.container_services[key][1].lower() == entity:
                    id_service = self.container_services[key][0]
                    break
                if key == (long_services - 1) and self.container_services[key][1].lower() != entity:
                    return "El servicio no se encuentra en la base de datos"
                else:
                    print("Se encontró el servicio")

        if asig == "Empleado":
            self.container_employee = self.database.employee()
            long_employee = len(self.container_employee)
            print(self.container_employee)
            print("len:", long_employee)

            #  Check that the employee entered is already in the database
            for key in range(long_employee):
                if self.container_employee[key][1].lower() == entity.lower():
                    id_employee = self.container_employee[key][0]
                    break
                if key == (long_employee - 1) and self.container_employee[key][1].lower() != entity.lower():
                    return "El empleado no se encuentra en la base de datos"
                print("no se encontró")

        maintenance_id = self.database.insert_maintenance(203040, id_employee, date)
        print(maintenance_id)

        for i in range(self.iterator):
            print(self.rv.data[i]['ide.text'], "-", self.rv.data[i]['name.text'])
        self.rv.data = []
        self.iterator = 0
        self.clear()

        return ""

    def delete(self):
        if self.rv.data:
            implement = self.rv.data[self.iterator - 1]['name.text']
            self.rv.data.pop(self.iterator - 1)
            self.iterator -= 1
            return f"{implement} fue eliminado"
        else:
            return ""

    def clear(self):
        self.message.text = self.nombre_add.text = ""
        self.id_up.text = self.name_up.text = ""
