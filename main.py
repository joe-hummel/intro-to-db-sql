import sqlite3
import logging
import sys
import datatier


##################################################
# main
#
print('starting')
print()

# eliminate traceback so we just get error message:
sys.tracebacklimit = 0

try:
  dbConn = sqlite3.connect("MovieLens.db")
  dbCursor = dbConn.cursor()
  
  # genre = input("Enter genre: ")
  
  sql = """
        Select Title, Round(avg(Rating),2) as Rating
        From Movies
        Inner Join Ratings on Movies.Movie_ID = Ratings.Movie_ID
        Inner Join Movie_Genres on Movies.Movie_ID = Movie_Genres.Movie_ID
        Inner Join Genres on Genres.Genre_ID = Movie_Genres.Genre_ID
        Where Genre_Name = 'Drama'
        Group By Ratings.Movie_ID
        Having Count(Rating) > 100
        Order By Rating DESC, Title ASC
        Limit 10;
        """
  
  dbCursor.execute(sql)
  rows = dbCursor.fetchall()
  
  for row in rows:
    print("Movie:", row[0], ", avg rating:", row[1]);

  dbCursor.close()
  dbConn.close()
  
except Exception as e:
  logging.error(e)

print()
print('done')


