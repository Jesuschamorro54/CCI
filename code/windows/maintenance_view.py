from kivy.uix.screenmanager import Screen, SlideTransition, RiseInTransition
from Proyect.database_conect.connect_database import *


class MaintenanceView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)