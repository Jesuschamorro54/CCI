from kivy.uix.screenmanager import ScreenManager, SlideTransition, RiseInTransition

from Proyect.database_conect.connect_database import *
from kivy.uix.screenmanager import Screen


class WindowMenu(Screen):
    def __init__(self, root, database, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)
        self.root = root
        self.database = database

    def ini(self):
        ide = self.database.logger
        print("ide desde menu:", ide)
        self.logger_name.text = self.database.employee_session(ide)

