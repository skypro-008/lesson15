import sqlite3
import prettytable

con = sqlite3.connect("../music.db")
cur = con.cursor()
sqlite_query = ("SELECT artists.name, albums.album_title FROM artists "
                "JOIN albums ON artists.ID = albums.artist_id")
table = cur.execute(sqlite_query)
mytable = prettytable.from_db_cursor(table)
mytable.max_width = 30

if __name__ == "__main__":
    print(mytable)
