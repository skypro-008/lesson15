#  В каких случаях используется LEFT JOIN на практике?
#  К примеру с его помощью можно определить у каких артистов нет ни одного альбома.
#  Попробуйте сами!
#  Выберите колонки name у артиста album_title у альбома и объедените их с помощью LEFT JOIN
#  Ознакомится со схемой базы данных можно в файле db_schema.png
#
#  ПОДСКАЗКА: (Вам потребуются таблицы Artists и Albums) а также конструкция с LEFT JOIN.
#  Также в этом задании вам потребуется дополнительное условие WHERE
#
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
