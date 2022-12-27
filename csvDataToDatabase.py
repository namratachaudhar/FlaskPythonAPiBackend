import pandas as pd
import pyodbc

# code to convert csv data into sql data using pandas and pyodbc 

# inserting movie data into database
def insertMovieData():
    data = pd.read_csv(
        r'C:\Users\NAMRATA\Desktop\React\Backend Coding Task\BackendCoding\sqlDatabaseFlaskProject\data\movies.csv')
    df = pd.DataFrame(data)
    print(df)

    connMovie = pyodbc.connect(
        'Driver={SQL Server};Server=.\SQLEXPRESS;Database=MoviesRatingData;Trusted_Connection=yes;')

    try:
        cursorMovie = connMovie.cursor()
        cursorMovie.execute('''
        CREATE TABLE movies (
			tconst nvarchar(50) primary key,
			titleType nvarchar(100),
            primaryTitle nvarchar(250),
            runtimeMinutes int,
            genres nvarchar(50)
			) ''')
        for row in df[0:].itertuples():
            cursorMovie.execute(''' INSERT INTO movies (tconst, titleType, primaryTitle, runtimeMinutes, genres) VALUES (?,?,?,?,?) ''',
                                row.tconst, row.titleType, row.primaryTitle, row.runtimeMinutes, row.genres)

        connMovie.commit()
        print('inserted data movies')

    except pyodbc.Error as err:
        print('Error !! %s' % err)
    except:
        print('something else failed ')

# inserting rating data into database
def insertRatingData():
    data = pd.read_csv(
        r'C:\Users\NAMRATA\Desktop\React\Backend Coding Task\BackendCoding\sqlDatabaseFlaskProject\data\ratings.csv')
    df = pd.DataFrame(data)
    print(df)

    connMovie = pyodbc.connect(
        'Driver={SQL Server};Server=.\SQLEXPRESS;Database=MoviesRatingData;Trusted_Connection=yes;')

    try:
        cursorMovie = connMovie.cursor()
        cursorMovie.execute('''
        CREATE TABLE ratings (
			tconst nvarchar(50) FOREIGN KEY REFERENCES movies(tconst),
			averageRating float,
            numVotes int
			) ''')
        for row in df[0:].itertuples():
            cursorMovie.execute(''' INSERT INTO ratings (tconst, averageRating, numVotes) VALUES (?,?,?) ''',
                                row.tconst, row.averageRating, row.numVotes)

        connMovie.commit()
        print('inserted data ratings')

    except pyodbc.Error as err:
        print('Error !! %s' % err)
    except:
        print('something else failed ')


insertRatingData()
