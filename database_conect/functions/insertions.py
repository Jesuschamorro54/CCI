def insert_address_func(cursor, address_values):
    # Print to check
    print("Inserting address...", address_values)

    # Query to run
    sql1 = f"INSERT INTO adress (calle, carrera, diagonal, transversal, numero, barrio)VALUES {address_values}"
    cursor.execute(sql1)
    print("The address was added")


def insert_employee_func(cursor, employee):
    # Print to check
    print("\nInserting employee...", employee)

    #  Query to run
    sql = f"INSERT INTO empleados(nombre, cargo, telefono, dir, fecha_inicio, fecha_final, estado)VALUE({employee}, null, 1)"
    cursor.execute(sql)
    print("The new employee was added")
