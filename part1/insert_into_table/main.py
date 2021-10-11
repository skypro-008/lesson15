# Добавление данных в таблицу
#
# Добавьте в БД следующих животных:
#
# +----+------------+-------+-----+-------------+-----+--------+
# | Id | AnimalType |  Name | Sex | DateOfBirth | Age | Weight |
# +----+------------+-------+-----+-------------+-----+--------+
# | 1  |   Кошка    |  Соня |  Ж  |  2013-12-02 |  7  |  2.15  |
# | 2  |    Кот     | Семен |  М  |  2017-05-03 |  4  |  4.5   |
# | 3  |   Собака   | Алина |  Ж  |  2018-11-12 |  2  |  20.8  |
# | 4  |    Пес     | Бобик |  М  |  2015-08-25 |  6  |  5.75  |
# +----+------------+-------+-----+-------------+-----+--------+
#
#
import sqlite3
import prettytable
from tools import create_table

con = sqlite3.connect(":memory:")
con = create_table(con)  # сформируем таблицу из предыдущих уроков
cur = con.cursor()
sqlite_query = ("")  # TODO составьте запрос на добавление данных в таблицу

# Не удаляйте этот код, он используется
# для вывода результата


def print_result(sqlite_query):
    cur.execute(sqlite_query)
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
