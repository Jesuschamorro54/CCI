from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, RiseInTransition
from Proyect.code.funtions_main.change_windows import *
from Proyect.database_conect.connect_database import *


class WindowLogin(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.database = DataBase("cci")
        self.container = dict(self.database.jobs())
        self.transition = SlideTransition(duration=.35)
        self.root = None

        # Employee login is validated

    def login(self, ide, post):
        try:
            ide = int(ide)
        except:
            return "Id de usuario debe ser un numero"
        self.container = dict(self.database.jobs())
        post_id = 0
        if ide == "":
            ide = "0"
        # first it is known what position the user entered
        for key in self.container:
            if self.container[key] == post:
                post_id = key
            else:
                pass
        # Then it is validated that the position
        # corresponds to the user or that the user exists in the database
        if self.database.valid_login(ide, post_id):
            go_menu_principal_func(self.root, self.transition)
            return ""
        else:
            return "Usuario ingresado no encontrado"

    # Returns in a list the names of the jobs
    def return_post(self):
        self.container = dict(self.database.jobs())
        job_name_list = []
        for key in self.container:
            job_name_list.append(self.container[key])
        return job_name_list

    def clear(self):
        self.cargo.text = ""
        self.text_notice.text = self.ide.text = ""
