# Cоздание таблицы со столбцом по умолчанию
#
# Создайте таблицу в БД на основе схемы из
# предыдущей задачи. При создании таблицы
# предусмотрите для поля Name значение по умолчанию "Noname"
#
import sqlite3
import prettytable

con = sqlite3.connect(":memory:")
cur = con.cursor()
sqlite_query = ("")  # TODO составьте запрос на создание таблицы
# Не удаляйте этот код, он используется
# для вывода заголовков созданной таблицы


def print_result(sqlite_query):
    cur.execute(sqlite_query)
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
