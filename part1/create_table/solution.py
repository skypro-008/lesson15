import sqlite3
import prettytable

con = sqlite3.connect(":memory:")
cur = con.cursor()
sqlite_query = ("CREATE TABLE animals ("
                "Id integer PRIMARY KEY AUTOINCREMENT, "
                "AnimalType varchar(50) NOT NULL, "
                "Sex varchar(50), "
                "Name varchar(50) NOT NULL DEFAULT 'Noname', "
                "DateOfBirth date,"
                "Age integer,"
                "Weight decimal)"
                )


def print_result(sqlite_query):
    cur.execute(sqlite_query)
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
