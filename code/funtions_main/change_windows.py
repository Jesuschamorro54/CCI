from Proyect.code.windows.hire_employee import HireEmployee


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
