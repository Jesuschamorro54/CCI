__autor__ = "Jesus Chamorro"

from Proyect.database_conect.connect_database import DataBase
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition, RiseInTransition
# from Proyect.code.windows.hire_employee import HireEmployee
from Proyect.code.windows.menu import Menu
from Proyect.code.funtions_main.change_windows import *
from Proyect.code.windows.buy_implement import AddImplement


# from kivy.properties import ObjectProperty
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.core.window import Window


# Initial window when executing the program

class Interface(App):

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)
        self.container = dict(database.jobs())
        self.signal = None
        self.menu = None

        self.root = None  # The root screen manager

    def build(self):
        self.menu = Menu(name="menu")
        self.root = ScreenManager(transition=self.transition)
        self.root.add_widget(self.menu)
        return self.root

    #  Go to hire employee
    def go_hire(self):
        go_hire_func(self.root, self.transition)

    def go_implement_view(self):
        go_implement_view_func(self.root, self.transition)

    def go_buy_implement(self):
        go_buy_implement_func(self.root, self.transition)

    #  Go back to menu
    def go_menu(self):
        self.transition.direction = 'right'
        self.root.current = 'menu'
        print("go to menu")



class Login(App):
    print("login")

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.container = None
        self.signal = 0

    def build(self):
        pass

    # Employee login is validated
    def login(self, ide, post):
        try:
            ide =  int(ide)
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
            login_app.signal = 1
            login_app.stop()
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


if __name__ == "__main__":
    # Instance database
    database = DataBase("cci")
    """"
    # Instance for interface
    login_app = Login()
    login_app.run()
    signal = login_app.signal

    # If "cancel" was pressed in the login window. Finish process
    if signal == 1:
        app = Interface()
        app.run()
    else:
        exit()
    """
    app = Interface()
    app.run()
