__autor__ = "Jesus Chamorro"

from kivy.app import App
from kivy.uix.screenmanager import SlideTransition, RiseInTransition
from Proyect.code.funtions_main.change_windows import *
from Proyect.code.windows.login import WindowLogin


# Initial window when executing the program

class Aplicacion(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)
        self.container = dict(database.jobs())
        self.container = None
        self.ide = 0
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
            go_menu_principal_func(self.root, self.transition)
            return ""
        else:
            return "The specified user was not found"

    # Returns in a list the names of the jobs
    def return_post(self):
        self.container = dict(database.jobs())
        job_name_list = []

        for key in self.container:
            job_name_list.append(self.container[key])

        return job_name_list

    def go_hire(self):
        print("ir a hire")
        go_hire_func(self.root, self.transition)

    def go_implement_view(self):
        go_implement_view_func(self.root, self.transition)

    def go_buy_implement(self):
        go_buy_implement_func(self.root, self.transition)

    def go_plan_maintenance(self):
        go_plan_maintenance_func(self.root, self.transition)

    def go_menu(self):
        self.transition.direction = 'right'
        self.root.current = 'menu'
        print("go to menu")

    def login_back(self):
        self.login_var.clear()
        self.transition.direction = 'right'
        self.root.current = 'login'
        print("go to menu")


if __name__ == "__main__":
    # Instance database
    database = DataBase("cci")

    # Instance for interface
    login_app = Aplicacion()
    login_app.run()
