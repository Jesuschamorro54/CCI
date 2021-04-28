def valid_login_func(cursor, ide, post):
    # print to check
    print("Validating\nid:", ide, "job:", post)

    # Query to run
    sql = f"select * from empleados where id={ide} and cargo={post}"
    cursor.execute(sql)
    try:
        if cursor.fetchone() is not None:
            print("Correct validation")
            return True
        else:
            return False
    except:
        return False


def valid_address(address):
    address = address.split(',')

    # check the data that will be sent to the address table
    for i in range(len(address)):
        if address[i] == '':
            address[i] = 'null'
        elif address[4] != 'null' or address[4] != "":
            try:
                address[4] = int(address[4])
            except:
                print("El valor no es tipo numerico")
                return 1
    if address[5] == 'null' or address[0] == 'null':
        return 2

    address_str = str(address)
    address_str = address_str.replace("['", "('")
    address_str = address_str.replace("']", "')")
    address_str = address_str.replace("'null'", "null")
    return address_str


def valid_insert_user(user):
    print("\nusuario: ", user)

    # validate that the data is complete

    if user[0] == '':
        print("nombre problem")
        return "Por favor ingrese un nombre"

    elif user[4] == 'YYYY-MM-DD' or user[4] == '' or len(user[4]) != 10:
        print("fecha problem")
        return "La fecha es incorrecta"

    elif user[2] == '':
        print("telefono vacio")
        user[2] = 'null'

    elif user[2] != '' or user[2] != 'null':
        print("cambiando a entero")
        print(len(user[2]))
        if 5 < len(user[2]) < 11:
            try:
                user[2] = int(user[2])
                print("cambiado: ", user[2])
            except:
                print("numero de telefono no valido")
                return "Numero de telefono incorrecto"
        else:
            return "Numero de telefono incorrecto"

    return user


def valid_date(date):
    if date == '' or len(date) != 10:
        print("Invalid date")
        return False

    list_date = date.split(sep='-')
    print(list_date)
    day = int(list_date[2])
    year = int(list_date[0])
    month = int(list_date[1])

    if not (1 <= day <= 31):
        print("Invalid day")
        return False
    elif not (1 <= month <= 12):
        print("Invalid month")
        return False
    elif year > 2021:
        print("Invalid year")
        return False

    return True
