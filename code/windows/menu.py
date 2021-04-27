from kivy.uix.screenmanager import ScreenManager, SlideTransition, RiseInTransition


from Proyect.database_conect.connect_database import *
from kivy.uix.screenmanager import Screen


class WindowMenu(Screen):
    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)
        self.root = root