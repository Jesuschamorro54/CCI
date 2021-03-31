
def insert_address_func(cursor, address_values):
    # Print to check
    print("Inserting address...", address_values)

    # Query to run
    sql1 = f"INSERT INTO adress (calle, carrera, diagonal, transversal, numero, barrio)VALUES {address_values}"
    cursor.execute(sql1)
    print("Se añadió")
