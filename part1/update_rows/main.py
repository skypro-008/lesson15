# Изменение данных
#
#
# Когда мы начали работать с получившейся таблицей,
# то поняли, что тип животных не стоит разделять по полу.
# Так что теперь нам нужно заменить
# в столбце AnimalType значение Кот на Кошка, Пес на Собака.
# Напишите соответствующий запрос.


import sqlite3
import prettytable
from tools import create_table

con = sqlite3.connect(":memory:")
con = create_table(con)  # сформируем таблицу из предыдущих уроков
cur = con.cursor()
sqlite_query_first = ("")  # TODO напишите здесь запрос на изменение строки
cur.execute(sqlite_query_first)
sqlite_query_second = ("")  # TODO напишите здесь запрос на изменение строки
cur.execute(sqlite_query_second)

# Не удаляйте этот код, он используется
# для вывода результата


def print_result():
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result()
