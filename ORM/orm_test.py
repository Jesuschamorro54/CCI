import peewee
import datetime

from past.builtins import raw_input

database = peewee.MySQLDatabase("cci", host='localhost', port='3306', user='root', password="20023006")


# Create table
class User(peewee.Model):
    username = peewee.CharField()
    email = peewee.CharField()
    create_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'User'


if __name__ == '__main__':
    if not User.table_exists():
        User.create_table()

    username = raw_input("Ingrese un nombre: ")
    email = raw_input("ingrese email: ")

    if not User.select().where(User.username == username).exist():
        insert = User.create(username=username, email=email)
        insert.save()
    else:
        print("Users Exist")
