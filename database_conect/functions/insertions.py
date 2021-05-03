from datetime import datetime


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
    sql = f"INSERT INTO implementos(nombre, belonging, proveedor, estado)VALUES({implement}, 7, {supplier}, -2)"
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

    date_now = datetime.now()
    date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"{supplier_id}, {implement_id}, {commodity}, '{date_now}'")

    # Query to run
    sql = f"INSERT INTO commodity(supplier, implement, cantidad, valor_unico, valor_total, fecha_pedido)VALUES({supplier_id}, {implement_id}, {commodity}, '{date_now}')"
    cursor.execute(sql)
    connection.commit()


def insert_maintenance_func(cursor, connection, authorized, assigned, date, option):
    # Print to check
    print("\nInserting maintenance...")

    # Query to run
    sql1 = f"INSERT INTO mantenimiento (authorized, assigned, programmed, estado)VALUES({authorized}, {assigned}, '{date}', -1)"
    sql2 = f"INSERT INTO mantenimiento (authorized, entity, programmed, estado)VALUES({authorized}, {assigned}, '{date}', -1)"

    if option == "employee":
        cursor.execute(sql1)
    else:
        cursor.execute(sql2)
    connection.commit()


def insert_recent_func(cursor, connection, authorized, maintenance, implement, option):
    # Print to check
    print("\nInserting recent...")

    date_now = datetime.now()
    date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")

    # Query to run
    sql1 = f"INSERT INTO recents (authorized, maintenance, implement, date)VALUES({authorized}, {maintenance}, {implement}, '{date_now}')"
    sql2 = f"INSERT INTO recents (authorized, maintenance, implement, date)VALUES({authorized}, {maintenance}, {implement}, '{date_now}') "

    if option == "employee":
        cursor.execute(sql1)
    else:
        cursor.execute(sql2)
    connection.commit()
