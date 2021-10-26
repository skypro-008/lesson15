# Удаление записи из БД
#
# Собака Алина давно перестала быть пациенткой ветклиники,
# так что нужно удалить запись о ней из базы.
# Реализовать соответствующий запрос.
#
#
import sqlite3
import prettytable
from tools import create_table

con = sqlite3.connect(":memory:")
con = create_table(con)  # сформируем таблицу из предыдущих уроков
cur = con.cursor()
sqlite_query = ("")  # TODO напишите здесь первый запрос на изменение строки

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
