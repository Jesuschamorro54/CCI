from kivy.uix.screenmanager import Screen
from Proyect.database_conect.connect_database import DataBase


class ImplementView(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container_implement = None
        self.container_area = None
        self.container_prov = None
        self.ide_implement = None

    def show(self):
        self.rv.data = [
            {
                'ide.text': str(self.container_implement[row][0]),
                'name.text': str(self.container_implement[row][1]),
                'area.text': str(self.container_area[self.container_implement[row][2]]),  # corregir problema
                'prov.text': str(self.container_implement[row][3]),
                'estado.text': str(self.container_implement[row][4]),
                'description.text': str(self.container_implement[row][5])
            } for row in range(len(self.container_implement))
        ]

    def show_all_record(self):
        self.container_implement = (self.database.implement(0, 1))
        self.container_area = dict(self.database.area())
        self.show()
        lon = len(self.container_implement)
        return f"{str(lon)} row(s) found"

    def search(self, seeker, identifier):
        self.clear()
        if identifier == 1 or identifier == 2:
            try:
                seeker = int(seeker)
            except:
                return "Invalid data"
        # if you are going to search through ID
        if identifier == 1:
            self.container_area = dict(self.database.area())
            self.container_implement = self.database.implement(seeker, 2)
            self.show()
        # if you are going to search through State
        if identifier == 2:
            self.container_area = dict(self.database.area())
            self.container_implement = (self.database.implement(seeker, 3))
            self.show()
        # if you are going to search through Area
        if identifier == 3:
            self.container_area = dict(self.database.area())
            self.container_implement = ""
            aux = 0
            for key in self.container_area:
                if self.container_area[key].lower() == seeker.lower():
                    self.container_implement = (self.database.implement(key, 4))
                    self.show()
                    aux = 1
            if aux == 0:
                return "It was not found"

        lon = len(self.container_implement)
        return f"{lon} row(s) found"

    # To sort
    def sort(self, identifier):
        if identifier == "Nombre":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['name.text'])
        elif identifier == "id":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['ide.text'])
        elif identifier == "Estado":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['estado.text'])
        elif identifier == "Area":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['area.text'])
        elif identifier == "Proveedor":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['prov.text'])

    # When is press the button update
    def update_state(self, ide, state):
        if not self.rv.data: return "No hay datos en la pantalla"
        if ide != "" and state != "":
            try:
                ide = int(ide)
                state = int(state)
                if not (-2 <= state <= 1):
                    return "Estado fuera del rango establecido"
            except:
                return "Hay datos invalidos"
            long = len(self.container_implement)
            print("long", long)
            for row in range(long):
                if self.container_implement[row][0] == ide:
                    self.database.update_implement(ide, state)
                    self.show_all_record()
                    self.change_state.text = self.change_id.text = ""
                    return ""
                if self.container_implement[row][0] != ide and row == long - 1:
                    return "El implemento no se encuentra en la base de datos"
        else:
            return ""

    def clear(self):
        self.rv.data = []
        self.container_implement = None
        self.container_area = None
