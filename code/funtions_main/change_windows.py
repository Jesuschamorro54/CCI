from Proyect.code.windows.hire_employee import *
from Proyect.code.windows.implement_view import *
from Proyect.code.windows.buy_implement import *
from Proyect.code.windows.plan_maintenance import *


def go_hire_func(root, transition):
    # If it returns an existing screen it just makes the change
    if root.has_screen(name="hire"):
        transition.direction = 'left'
        root.current = "hire"
        print("go to hire again")
    else:
        hire = HireEmployee(name="hire")
        print("go to hire")
        root.add_widget(hire)
        transition.direction = 'left'
        root.current = hire.name


def go_implement_view_func(root, transition):
    if root.has_screen(name="implement_view"):
        transition.direction = 'left'
        root.current = "implement_view"
        print("go to implement view again")
    else:
        imp = ImplementView(name="implement_view")
        print("go to implement view")
        root.add_widget(imp)
        transition.direction = 'left'
        root.current = imp.name


def go_buy_implement_func(root, transition):
    if root.has_screen(name="buy_implement"):
        transition.direction = 'left'
        root.current = "buy_implement"
        print("go to buy implement again")
    else:
        b_imp = AddImplement(name="buy_implement")
        print("go to buy implement")
        root.add_widget(b_imp)
        transition.direction = 'left'
        root.current = b_imp.name


def go_plan_maintenance_func(root, transition, logger):
    if root.has_screen(name="plan"):
        transition.direction = 'left'
        root.current = "plan"
        print("go to plan maintenance")
    else:
        b_imp = PlanMaintenance(name="plan", logger=logger)
        print("go to plan maintenance")
        root.add_widget(b_imp)
        transition.direction = 'left'
        root.current = b_imp.name
