from kivy.uix.screenmanager import ScreenManager, SlideTransition, RiseInTransition
from Proyect.code.funtions_main.change_windows import *
from kivy.uix.screenmanager import Screen


class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=.35)
        self.transition_menu = RiseInTransition()
        self.signal = None
        self.menu = None

        self.root = None  # The root screen manager

        #  Change windows  #

    def go_hire(self):
        go_hire_func(self.root, self.transition)

    def go_implement_view(self):
        go_implement_view_func(self.root, self.transition)

    def go_buy_implement(self):
        go_buy_implement_func(self.root, self.transition)

    def go_plan_maintenance(self):
        go_plan_maintenance_func(self.root, self.transition, self.logger)

    def go_menu_principal(self):
        go_menu_principal(self.root)

        # Go back to menu

    def go_menu(self):
        self.transition.direction = 'right'
        self.root.current = 'menu'
        print("go to menu")
