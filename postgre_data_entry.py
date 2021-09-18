from main import Movie, db
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


certificate = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
cred = credentials.Certificate(certificate)
firebase_admin.initialize_app(cred)
fdb = firestore.client()


def read_data():
    movies = list(fdb.collection(u'movies').stream())
    return movies


movies = read_data()
for movie_data in movies:
    movie = movie_data.to_dict()
    new_movie = Movie(
        movieId=movie['movieId'],
        title=movie['title'],
        originalTitle=movie['originalTitle'],
        year=movie['year'],
        genres=movie['genres'],
        director=movie['director'],
        writer=movie['writer'],
        actors=movie['actors'],
        plot=movie['plot'],
        poster=movie['poster'],
        imdbRating=movie['imdbRating'],
        imdbVotes=movie['imdbVotes'],
        imdbID=movie['imdbID']
    )
    db.session.add(new_movie)

db.session.commit()
print("Completed")
