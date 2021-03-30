def insert_address_func(cursor, address_values):
    # Print to check
    print("Inserting address...", address_values)

    # Query to run
    sql = f"INSERT INTO adress (calle, carrera, diagonal, transversal, numero, barrio)VALUES {address_values}"
    id = "SELECT last_insert_id()"
    cursor.execute(sql)
    print("Se añadió")
