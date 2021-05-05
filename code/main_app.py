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
        self.login_ins = None
        self.logger = None
        self.root = None  # The root screen manager

    def build(self):
        self.login_ins = WindowLogin(name="login")
        self.root = ScreenManager(transition=self.transition)
        self.root.add_widget(self.login_ins)
        self.login_ins.root = self.root
        self.login_ins.transition = self.transition
        return self.root

    def go_hire(self):
        go_hire_func(self.root, self.transition)

    def go_implement_view(self):
        go_implement_view_func(self.root, self.transition)

    def go_buy_implement(self):
        go_buy_implement_func(self.root, self.transition)

    def go_plan_maintenance(self):
        go_plan_maintenance_func(self.root, self.transition, self.login_ins.database)

    def go_maintenance_view(self):
        go_maintenance_view_func(self.root, self.transition)

    def go_menu(self):
        self.transition.direction = 'right'  # derecha
        self.root.current = 'menu'
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [BACK TO MENU    ]{Color.RESET}")

    def login_back(self):
        self.transition.direction = 'down'
        self.root.current = 'login'
        self.login_ins.logger = ""
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [BACK TO LOGIN   ]{Color.RESET}")


if __name__ == "__main__":
    # Instance database
    database = DataBase("cci")

    # Instance for interface
    login_app = Aplicacion()
    login_app.run()
