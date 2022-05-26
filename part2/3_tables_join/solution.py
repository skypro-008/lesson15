import sqlite3
import prettytable

con = sqlite3.connect("../music.db")
cur = con.cursor()
sqlite_query = ("SELECT DISTINCT artists.Name, genres.Name as genre "
                "FROM artists JOIN albums ON artists.ID = albums.artist_id "
                "JOIN tracks ON albums.ID = tracks.album_id "
                "JOIN genres ON genres.ID = tracks.genre_id")
table = cur.execute(sqlite_query)
mytable = prettytable.from_db_cursor(table)
mytable.max_width = 30

if __name__ == "__main__":
    print(mytable)
