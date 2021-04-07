def insert_address_func(cursor, address_values, connection):
    # Print to check
    print("Inserting address...", address_values)

    # Query to run
    sql = f"INSERT INTO adress (calle, carrera, diagonal, transversal, numero, barrio)VALUES {address_values}"
    cursor.execute(sql)
    connection.commit()
    print("The address was added")


def insert_employee_func(cursor, employee, connection):
    # Print to check
    print("\nInserting employee...", employee)

    #  Query to run
    sql = f"INSERT INTO empleados(nombre, cargo, telefono, dir, fecha_inicio, fecha_final, estado)VALUE({employee}, null, 1)"
    cursor.execute(sql)
    connection.commit()
    print("The new employee was added")


def insert_implement_func(cursor, implement, supplier, connection):
    # Print to check
    print("\nInserting implement...")

    # Query to run
    sql = f"INSERT INTO implementos(nombre, proveedor, estado)VALUES({implement}, {supplier}, -2)"
    cursor.execute(sql)
    connection.commit()


def insert_supplier_func(cursor, supplier, connection):
    # Print to check
    print("\nInserting supplier...", supplier)

    # Query to run
    sql = f"INSERT INTO proveedores(nombre, telefono, tipo, bodega)VALUES('{supplier}', null, 0, null)"
    cursor.execute(sql)
    connection.commit()


def insert_commodity_func(cursor, implement_id, supplier_id, commodity, connection):
    # Print to check
    print("\nInsert commodity...")

    # Query to run
    sql = f"INSERT INTO commodity(supplier, implement, cantidad, valor_unico, valor_total, fecha)VALUES({supplier_id}, {implement_id}, {commodity})"
    cursor.execute(sql)
    connection.commit()


