import sqlite3
import prettytable
from tools import create_table

con = sqlite3.connect(":memory:")
con = create_table(con)
cur = con.cursor()
sqlite_query = (
    "INSERT INTO 'animals' "
    "('AnimalType', 'Sex', 'Name', 'DateOfBirth', 'Age', 'Weight') VALUES "
    "('Кошка', 'Ж', 'Соня', '2013-12-02', 7, 2.15),"
    "('Кот', 'М', 'Семен', '2017-05-03', 4, 4.5),"
    "('Собака', 'Ж', 'Алина', '2018-11-12', 2, 20.8),"
    "('Пес', 'М', 'Бобик', '2015-08-25', 6, 5.75)"
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
