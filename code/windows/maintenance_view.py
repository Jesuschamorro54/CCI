from kivy.uix.screenmanager import Screen, SlideTransition, RiseInTransition
from Proyect.database_conect.connect_database import *


class MaintenanceView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)

    def show(self):
        self.rv.data = [
            {
                'ide.text': str(self.container_implement[row][0]),
                'authorized.text': str(self.container_implement[row][1]),
                'entity.text': str(self.container_area[self.container_implement[row][2]]),  # corregir problema
                'assigned.text': str(self.container_implement[row][3]),
                'id_maint.text': str(self.container_implement[row][4]),
                'implement.text': str(self.container_implement[row][5]),
                'date.text': str(self.container_implement[row][6]),
                'programmed.text': str(self.container_implement[row][7])

            } for row in range(len())  # Edit
        ]