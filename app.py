from flask import Flask, request
from DatabaseConnectionApi import DataConnection


app = Flask(__name__)
newData = DataConnection()


@app.get('/api/v1/longest-duration-movies')
def get_LongestMovieRunAPI():
    result = newData.get_LongestMovieRun()
    if len(result) != 0:
        return {"message": result}
    else:
        return {"message": "Item not found"}


@app.get('/movies')
def get_MovieAPI():
    result = newData.get_DataMovie()
    if len(result) != 0:
        return {"message": result}
    else:
        return {"message": "Item not found"}


@app.post('/api/v1/new-movie')
def post_MovieAPI():
    jData = request.get_json()
    print(jData)
    if "tconst" not in jData or "titleType" not in jData or "primaryTitle" not in jData or "runtimeMinutes" not in jData or "genres" not in jData:
        return {"message": "Provide the valid json inputs : tconst, titleType, primaryTitle, runtimeMinutes, genres"}
    else:
        newData.postDataIntoMovies(jData)
        return {"message": "Success"}

@app.get('/api/v1/top-rated-movies')
def get_avgRating():
    result = newData.avgRatingOfMovies()
    return {"message": result}

