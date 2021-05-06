from kivy.uix.screenmanager import ScreenManager, RiseInTransition
from Proyect.code.windows.menu import WindowMenu
from Proyect.code.windows.hire_employee import *
from Proyect.code.windows.implement_view import *
from Proyect.code.windows.buy_implement import *
from Proyect.code.windows.plan_maintenance import *
from Proyect.code.windows.maintenance_view import *
from Proyect.database_conect.connect_database import Color


def go_hire_func(root, transition):
    # If it returns an existing screen it just makes the change
    if root.has_screen(name="hire"):
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [HIRE EMPLOYEE   ]{Color.RESET}")
        transition.direction = 'left'
        root.current = "hire"
    else:
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [HIRE EMPLOYEE   ]{Color.RESET}")
        hire = HireEmployee(name="hire")
        root.add_widget(hire)
        transition.direction = 'left'
        root.current = hire.name


def go_implement_view_func(root, transition):
    if root.has_screen(name="implement_view"):
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [IMPLEMENT VIEW  ]{Color.RESET}")
        transition.direction = 'left'
        root.current = "implement_view"

    else:
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [IMPLEMENT VIEW  ]{Color.RESET}")
        imp = ImplementView(name="implement_view")
        root.add_widget(imp)
        transition.direction = 'left'
        root.current = imp.name


def go_buy_implement_func(root, transition):
    if root.has_screen(name="buy_implement"):
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [BUY IMPLEMENT   ]{Color.RESET}")
        transition.direction = 'left'
        root.current = "buy_implement"
    else:
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [BUY IMPLEMENT   ]{Color.RESET}")
        b_imp = AddImplement(name="buy_implement")
        root.add_widget(b_imp)
        transition.direction = 'left'
        root.current = b_imp.name


def go_plan_maintenance_func(root, transition, db):
    if root.has_screen(name="plan"):
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [PLAN MAINTENANCE]{Color.RESET}")
        transition.direction = 'left'
        root.current = "plan"
    else:
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [PLAN MAINTENANCE]{Color.RESET}")
        window = PlanMaintenance(name="plan", database=db)
        root.add_widget(window)
        transition.direction = 'left'
        root.current = window.name


def go_maintenance_view_func(root, transition):
    if root.has_screen(name="view_maintenance"):
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [MAINTENANCE VIEW]{Color.RESET}")
        transition.direction = 'left'
        root.current = "view_maintenance"
    else:
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [MAINTENANCE VIEW]{Color.RESET}")
        window = MaintenanceView(name="view_maintenance")
        root.add_widget(window)
        transition.direction = 'left'
        root.current = window.name


def go_menu_principal_func(root, transition, db):
    if root.has_screen(name="menu"):
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [GO MENU         ]{Color.RESET}")
        transition.direction = 'up'
        root.current = "menu"
    else:
        print(f"{Color.GREEN}[CHANGE SCREEN] --> [GO MENU         ]{Color.RESET}")
        go_menu = WindowMenu(name="menu", root=root, database=db)
        root.add_widget(go_menu)
        transition.direction = 'up'
        root.current = go_menu.name
