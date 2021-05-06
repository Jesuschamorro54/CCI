from kivy.uix.screenmanager import Screen, SlideTransition
from Proyect.database_conect.connect_database import *
from Proyect.database_conect.functions.validate import *


class MaintenanceView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)
        self.database = DataBase("cci")
        self.data = None
        self.container_assigned = None

    def show(self):
        self.rv.data = [
            {
                'ide.text': str(self.data[row][0]),
                'authorized.text': str(self.data[row][1]),
                'entity.text': str("-"if self.data[row][2] is None else self.data[row][2]),
                'assigned.text': str("-"if self.data[row][3] is None else self.container_assigned[self.data[row][3]]),
                'id_maint.text': str(self.data[row][4]),
                'implement.text': str(self.data[row][5]),
                'date.text': str(self.data[row][6]),
                'programmed.text': str(self.data[row][7])

            } for row in range(len(self.data))  # Edit
        ]

    def show_all(self):
        self.data = self.database.maintenance(0, 4)
        self.database.cursor.execute("select id, nombre from empleados")
        content = self.database.cursor.fetchall()
        self.container_assigned = dict(content)
        self.show()
        self.seeker.text = ""
        lon = len(self.data)
        return f"{str(lon)} row(s) found"

    def sort(self, identifier):
        if identifier == "ID":
            self.rv.data = sorted(self.rv.data, key=lambda x: int(x['ide.text']))
        elif identifier == "Autoriza":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['authorized.text'])
        elif identifier == "Entidad":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['entity.text'])
        elif identifier == "Asignado":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['assigned.text'])
        elif identifier == "ID MANT":
            self.rv.data = sorted(self.rv.data, key=lambda x: int(x['id_maint.text']))
        elif identifier == "Implemento":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['implement.text'])
        elif identifier == "Solicitud":
            self.rv.data = sorted(self.rv.data, key=lambda x: x['date.text'])
        else:
            self.rv.data = sorted(self.rv.data, key=lambda x: x['programmed.text'])

    def search(self, identifier, seeker):
        self.clear()
        if identifier == "ID MANT":
            try:
                seeker = int(seeker)
            except:
                return "Invalid data"
        if identifier == "Date":
            if valid_date(seeker):
                self.data = self.database.maintenance(seeker, 1)  # search by date on Database
                self.database.cursor.execute("select id, nombre from empleados")
                content = self.database.cursor.fetchall()
                self.container_assigned = dict(content)
                self.show()
            else: return ""
        elif identifier == "Implement":
            if seeker != "":
                self.data = self.database.maintenance(seeker, 2)  # search by date on Database
                self.database.cursor.execute("select id, nombre from empleados")
                content = self.database.cursor.fetchall()
                self.container_assigned = dict(content)
                self.show()
            else: return ""
        else:
            if seeker != "":
                self.data = self.database.maintenance(seeker, 3)  # search by date on Database
                self.database.cursor.execute("select id, nombre from empleados")
                content = self.database.cursor.fetchall()
                self.container_assigned = dict(content)
                self.show()
            else: return ""
        self.seeker.text = ""
        lon = len(self.data)
        return f"{str(lon)} row(s) found"

    def clear(self):
        self.rv.data = []
        self.container_assigned = None
        self.data = None
