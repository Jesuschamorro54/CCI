__autor__ = "Jesus Chamorro"

from kivy.app import App
from kivy.uix.screenmanager import SlideTransition, RiseInTransition
from Proyect.code.funtions_main.change_windows import *
from Proyect.code.windows.login import *


# Initial window when executing the program

class Login(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.transition = SlideTransition(duration=.35)
        self.transition_menu = RiseInTransition()
        self.container = dict(database.jobs())
        self.container = None
        self.signal = 0
        self.ide = 0
        self.signal = None
        self.login_var = None

        self.root = None  # The root screen manager

    def build(self):
        self.login_var = WindowLogin(name="login")
        self.root = ScreenManager(transition=self.transition)
        self.root.add_widget(self.login_var)
        return self.root

        # Employee login is validated

    def login(self, ide, post):
        try:
            ide = int(ide)
        except:
            return "User id must be of type integer "

        self.container = dict(database.jobs())
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
        if database.valid_login(ide, post_id):
            self.go_menu_principal()
            return "OK"
        else:
            return "The specified user was not found"

    # Returns in a list the names of the jobs
    def return_post(self):
        self.container = dict(database.jobs())
        job_name_list = []

        for key in self.container:
            job_name_list.append(self.container[key])

        return job_name_list

    #  Change windows  #
    def go_menu_principal(self):
        go_menu_principal(self.root)


class Loginn(App):
    pass


if __name__ == "__main__":
    # Instance database
    database = DataBase("cci")

    # Instance for interface
    login_app = Login()
    login_app.run()
