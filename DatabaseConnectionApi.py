import pyodbc

class DataConnection:
    def __init__(self):
        self.conn = pyodbc.connect(
            'Driver={SQL Server};Server=.\SQLEXPRESS;Database=MoviesRatingData;Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def get_DataMovie(self):
        query = "Select * from movies"
        self.cursor.execute(query)
        result = []
        rows = self.cursor.fetchall()
        for row in rows:
            dict = {}

            dict["tconst"] = row[0]
            dict["titleType"] = row[1],
            dict["primaryTitle"] = row[2]
            dict["runtimeMinutes"] = row[3]
            dict["genres"] = row[4]
            result.append(dict)
        return result

    def get_LongestMovieRun(self):
        query = "Select TOP 10 tconst, primaryTitle, runtimeMinutes,genres from movies ORDER BY runtimeMinutes DESC"
        self.cursor.execute(query)
        result = []
        rows = self.cursor.fetchall()
        for row in rows:
            dict = {}
            dict["tconst"] = row[0]
            dict["primaryTitle"] = row[1]
            dict["runtimeMinutes"] = row[2]
            dict["genres"] = row[3]
            result.append(dict)
        return result

    def postDataIntoMovies(self, data):
        query = f"INSERT INTO movies (tconst, titleType, primaryTitle, runtimeMinutes, genres) VALUES ('{data['tconst']}', '{data['titleType']}','{data['primaryTitle']}',{data['runtimeMinutes']},'{data['genres']}')"
        self.cursor.execute(query)
        self.conn.commit()

    def avgRatingOfMovies(self):
        query = "SELECT movies.tconst, movies.primaryTitle, movies.genres, ratings.averageRating FROM movies INNER JOIN ratings ON movies.tconst = ratings.tconst WHERE (ratings.averageRating)> 6.0 ORDER BY ratings.averageRating"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            dict = {}
            dict["tconst"] = row[0],
            dict["primaryTitle"] = row[1],
            dict["genres"] = row[2],
            dict["averageRating"] = row[3]
            result.append(dict)
        return result
