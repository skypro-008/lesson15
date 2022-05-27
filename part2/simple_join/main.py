# Используя JOIN выведите все песни(title) и название альбомов (album_title) группы
# Red Hot Chili Peppers, содержащиеся в базе.
# Вам потребуются таблицы tracks и albums
# Ознакомится со схемой базы данных можно в файле db_schema.png

import sqlite3
import prettytable

con = sqlite3.connect("../music.db")
cur = con.cursor()
sqlite_query = ("")  # TODO составьте запрос на создание таблицы


# Не удаляйте код ниже, он используется
# для вывода заголовков созданной таблицы
table = cur.execute(sqlite_query)
mytable = prettytable.from_db_cursor(table)
mytable.max_width = 30

if __name__ == "__main__":
    print(mytable)
