from Proyect.code.windows.hire_employee import HireEmployee
from Proyect.code.windows.implement_view import ImplementView


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
    if root.has_screen(name="implement"):
        transition.direction = 'left'
        root.current = "implement"
        print("go to implement view again")
    else:
        imp = ImplementView(name="implement")
        print("go to implement view")
        root.add_widget(imp)
        transition.direction = 'left'
        root.current = imp.name
