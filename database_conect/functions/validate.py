def valid_login_func(cursor, ide, post):
    # print to check
    print("Validating\nid:", ide, "job:", post)

    # Query to run
    sql= f"select * from empleados where id={ide} and cargo={post}"
    cursor.execute(sql)
    try:
        if cursor.fetchone() is not None:
            print("Correct validation")
            return True
        else:
            return False
    except:
        pass
