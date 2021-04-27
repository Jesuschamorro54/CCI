__autor__ = "Jesus Chamorro"

from kivy.app import App
from kivy.uix.screenmanager import SlideTransition, RiseInTransition
from Proyect.code.funtions_main.change_windows import *
from Proyect.code.windows.login import WindowLogin
from Proyect.database_conect.connect_database import *


# Initial window when executing the program

class Aplicacion(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)
        self.container = None
        self.ide = 0
        self.login_var = None
        self.logger = None
        self.root = None  # The root screen manager

    def build(self):
        self.login_var = WindowLogin(name="login")
        self.root = ScreenManager(transition=self.transition)
        self.root.add_widget(self.login_var)
        self.login_var.root = self.root
        self.logger = self.login_var.logger
        return self.root

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
        self.login_var.logger = ""
        print("go to login")

    def session(self):
        print("ESTE ES EL LOGGER: ", self.login_var.logger)
        return database.employee_session(self.login_var.logger)


if __name__ == "__main__":
    # Instance database
    database = DataBase("cci")

    # Instance for interface
    login_app = Aplicacion()
    login_app.run()
