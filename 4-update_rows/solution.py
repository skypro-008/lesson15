import sqlite3
import prettytable
from tools import create_table

con = sqlite3.connect(":memory:")
con = create_table(con)
cur = con.cursor()
sqlite_query = (
    "BEGIN; "
    "UPDATE animals SET `AnimalType`='Кошка' WHERE `Name`='Семен';"
    "UPDATE animals SET `AnimalType`='Собака' WHERE `Name`='Бобик';"
    "END;"
)


def print_result(sqlite_query):
    cur.executescript(sqlite_query)
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
