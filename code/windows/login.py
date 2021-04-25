from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, RiseInTransition
from Proyect.code.funtions_main.change_windows import *


class WindowLogin(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def clear(self):
        self.cargo.text = "deploy"
        self.text_notice.text = self.id_identification.text = ""