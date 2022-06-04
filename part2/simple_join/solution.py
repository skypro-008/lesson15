import sqlite3
import prettytable

con = sqlite3.connect("../music.db")
cur = con.cursor()
sqlite_query = (
    "SELECT tracks.title, albums.album_title as album_title FROM tracks "
    "JOIN albums ON tracks.album_id = albums.ID "
    "WHERE tracks.Author='Red Hot Chili Peppers'")
table = cur.execute(sqlite_query)
mytable = prettytable.from_db_cursor(table)
mytable.max_width = 30

if __name__ == "__main__":
    print(mytable)
