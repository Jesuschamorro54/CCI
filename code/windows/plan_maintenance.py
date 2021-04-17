from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase


# noinspection PyCompatibility
class PlanMaintenance(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.iterator = 0

    def add(self, value):
        if value == "":
            return
        print("add...")
        self.rv.data.insert(self.iterator, {'name.text': value, 'ide.text': str(self.iterator)})
        self.iterator += 1

    def update(self, ide, name_text):
        if ide == "" or name_text == "":
            return
        ide = int(ide)
        if self.rv.data:
            self.rv.data[ide]['name.text'] = name_text
            self.rv.refresh_from_data()
        print(self.rv.data[ide]['name.text'])

    def delete(self):
        if self.rv.data:
            self.rv.data.pop(self.iterator-1)
            self.iterator -= 1